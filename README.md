# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--18_02:33:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **182,301 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 02:33:50 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:33:22 | Urawa (Nilwala Ganga) | 1.19 | 🟢 Normal | -0.063 |  |
| 2026-06-18 02:27:23 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:16:39 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:13:38 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-06-18 02:13:36 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-06-18 02:12:36 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:11:35 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-06-18 02:11:15 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:09:19 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 02:07:27 | Dunamale (Aththanagalu Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:06:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-18 02:06:16 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.057 |  |
| 2026-06-18 02:06:13 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:06:04 | Hanwella (Kelani Ganga) | 2.67 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-06-18 02:05:05 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:05:00 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:04:33 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.101 |  |
| 2026-06-18 02:04:29 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:03:54 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-18 02:03:38 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | -0.096 |  |
| 2026-06-18 02:02:52 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:02:41 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-06-18 02:02:12 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:02:06 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:01:51 | Peradeniya (Mahaweli Ganga) | 2.39 | 🟢 Normal | -0.118 |  |
| 2026-06-18 02:01:28 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 02:01:24 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.046 |  |
| 2026-06-18 02:01:14 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-18 02:00:54 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.017 |  |
| 2026-06-18 01:58:45 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 02:13:38 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-06-18 02:06:04 | Hanwella (Kelani Ganga) | 2.67 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-06-18 02:02:41 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-06-18 02:11:35 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-06-18 01:04:22 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-06-18 00:06:04 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-18 02:06:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-18 00:12:09 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-18 02:03:54 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-18 02:01:28 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 02:09:19 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 18:02:56 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:27:23 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:02:52 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:02:06 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:05:05 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:04:29 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:02:12 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:11:15 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:05:00 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:02:24 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-18 01:14:00 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:07:27 | Dunamale (Aththanagalu Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:33:50 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:16:39 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:06:13 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:12:36 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:05:17 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-06-18 02:01:14 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:01:25 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-18 02:00:54 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.017 |  |
| 2026-06-18 02:01:24 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.046 |  |
| 2026-06-18 02:06:16 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.057 |  |
| 2026-06-18 02:33:22 | Urawa (Nilwala Ganga) | 1.19 | 🟢 Normal | -0.063 |  |
| 2026-06-18 01:05:28 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.067 |  |
| 2026-06-18 02:03:38 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | -0.096 |  |
| 2026-06-18 02:04:33 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.101 |  |
| 2026-06-18 02:01:51 | Peradeniya (Mahaweli Ganga) | 2.39 | 🟢 Normal | -0.118 |  |
| 2026-06-18 01:05:32 | Rathnapura (Kalu Ganga) | 2.81 | 🟢 Normal | -0.163 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)