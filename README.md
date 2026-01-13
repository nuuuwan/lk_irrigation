# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--13_11:15:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **44,410 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 11:15:19 | Yaka Wewa (Ma Oya) | 1.36 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-13 11:14:23 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:13:48 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:11:48 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | -0.026 |  |
| 2026-01-13 11:08:37 | Glencourse (Kelani Ganga) | 8.96 | 🟢 Normal | -0.028 |  |
| 2026-01-13 11:07:44 | Horowpothana (Yan Oya) | 3.75 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-13 11:07:32 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:06:28 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.019 |  |
| 2026-01-13 11:06:24 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:06:17 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-01-13 11:05:19 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:05:00 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | -0.011 |  |
| 2026-01-13 11:04:31 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-13 11:04:20 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.158 |  |
| 2026-01-13 11:04:13 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:04:05 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-13 11:04:04 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-13 11:03:55 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:03:55 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:03:41 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 11:03:40 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:03:19 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-13 11:02:48 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.042 |  |
| 2026-01-13 11:02:32 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:02:32 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:02:22 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | -0.030 |  |
| 2026-01-13 11:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-01-13 11:02:19 | Baddegama (Gin Ganga) | 0.76 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-13 11:02:01 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:01:58 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:01:39 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-13 11:01:29 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:01:25 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-01-13 11:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-13 11:01:13 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | -0.021 |  |
| 2026-01-13 11:00:57 | Thanthirimale (Malwathu Oya) | 2.64 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-13 11:00:56 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-01-13 11:00:23 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.010 |  |
| 2026-01-13 11:00:18 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 11:01:25 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-01-13 11:02:19 | Baddegama (Gin Ganga) | 0.76 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-13 11:15:19 | Yaka Wewa (Ma Oya) | 1.36 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-13 11:00:57 | Thanthirimale (Malwathu Oya) | 2.64 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-13 11:07:44 | Horowpothana (Yan Oya) | 3.75 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-13 11:03:19 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-13 11:03:41 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 11:02:32 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:01:58 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-13 10:01:52 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:00:18 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:03:55 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:06:24 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:01:29 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:04:13 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:03:55 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:02:32 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:07:32 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:03:40 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:14:23 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:05:19 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:13:48 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:04:04 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-13 11:04:31 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-13 11:04:05 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-13 11:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-13 11:06:17 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-01-13 11:00:23 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.010 |  |
| 2026-01-13 11:01:39 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-13 11:00:56 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-01-13 11:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-01-13 11:05:00 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | -0.011 |  |
| 2026-01-13 11:06:28 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.019 |  |
| 2026-01-13 11:01:13 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | -0.021 |  |
| 2026-01-13 11:11:48 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | -0.026 |  |
| 2026-01-13 11:08:37 | Glencourse (Kelani Ganga) | 8.96 | 🟢 Normal | -0.028 |  |
| 2026-01-13 11:02:22 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | -0.030 |  |
| 2026-01-13 11:02:48 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.042 |  |
| 2026-01-13 11:04:20 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.158 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)