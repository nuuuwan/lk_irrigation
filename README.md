# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--18_01:35:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **182,270 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 01:35:23 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-18 01:14:00 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:11:05 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:09:29 | Panadugama (Nilwala Ganga) | 3.58 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-06-18 01:08:34 | Hanwella (Kelani Ganga) | 2.52 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-06-18 01:07:35 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | 6.207 | 🔺 Rising |
| 2026-06-18 01:07:10 | Glencourse (Kelani Ganga) | 11.44 | 🟢 Normal | -0.051 |  |
| 2026-06-18 01:07:06 | Urawa (Nilwala Ganga) | 1.23 | 🟢 Normal | 6.207 | 🔺 Rising |
| 2026-06-18 01:06:22 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-18 01:05:53 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-18 01:05:37 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-06-18 01:05:32 | Rathnapura (Kalu Ganga) | 2.81 | 🟢 Normal | -0.163 |  |
| 2026-06-18 01:05:28 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.067 |  |
| 2026-06-18 01:04:58 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.109 |  |
| 2026-06-18 01:04:34 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:04:30 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:04:22 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-06-18 01:03:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.010 |  |
| 2026-06-18 01:03:29 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:03:01 | Dunamale (Aththanagalu Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:02:52 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-18 01:02:39 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:02:39 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:02:32 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:02:27 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:02:24 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:02:19 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:02:14 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:01:32 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-18 01:01:19 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:00:53 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 01:07:35 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | 6.207 | 🔺 Rising |
| 2026-06-18 01:08:34 | Hanwella (Kelani Ganga) | 2.52 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-06-18 01:05:37 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-06-18 01:09:29 | Panadugama (Nilwala Ganga) | 3.58 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-06-18 01:04:22 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-06-18 01:02:52 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-18 00:06:04 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-18 01:05:53 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-18 00:12:09 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-18 01:01:32 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-18 01:06:22 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-18 01:35:23 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-17 23:05:06 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.005 |  |
| 2026-06-17 18:02:56 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:02:19 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-18 00:03:15 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:02:14 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:02:27 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:02:39 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-18 00:09:06 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:02:39 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:04:30 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:02:24 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:14:00 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:03:01 | Dunamale (Aththanagalu Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:00:53 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-18 00:04:02 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:04:34 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:03:29 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:01:19 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:11:05 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:05:17 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:01:25 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-18 01:03:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.010 |  |
| 2026-06-18 00:16:02 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.019 |  |
| 2026-06-18 01:07:10 | Glencourse (Kelani Ganga) | 11.44 | 🟢 Normal | -0.051 |  |
| 2026-06-18 01:05:28 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.067 |  |
| 2026-06-18 01:04:58 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.109 |  |
| 2026-06-18 01:05:32 | Rathnapura (Kalu Ganga) | 2.81 | 🟢 Normal | -0.163 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)