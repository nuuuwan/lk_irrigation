# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_06:22:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **128,143 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 06:22:35 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.008 |  |
| 2026-04-18 06:12:41 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:12:03 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.061 |  |
| 2026-04-18 06:09:28 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:09:25 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-18 06:08:46 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:08:21 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.072 |  |
| 2026-04-18 06:06:44 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:05:54 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:05:44 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:05:13 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.065 |  |
| 2026-04-18 06:05:04 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-18 06:04:28 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:04:26 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:03:51 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:03:45 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:03:04 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.162 |  |
| 2026-04-18 06:02:46 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:02:36 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-18 06:02:32 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.115 |  |
| 2026-04-18 06:02:32 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:02:20 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:02:14 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:02:13 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-04-18 06:02:06 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-04-18 06:01:50 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:01:43 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:01:32 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:01:31 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:01:13 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:01:12 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-18 06:01:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.316 | 🔺 Rising |
| 2026-04-18 06:00:39 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:00:12 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 06:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.042 |  |
| 2026-04-18 06:00:02 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-18 05:52:10 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-18 05:47:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.81 | 🟢 Normal | 0.316 | 🔺 Rising |
| 2026-04-18 05:41:44 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.115 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 06:01:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.316 | 🔺 Rising |
| 2026-04-18 06:02:06 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-04-18 06:09:25 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-18 06:05:04 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-18 06:02:36 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-18 06:01:12 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-18 04:06:02 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-18 06:00:12 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 06:03:45 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:02:46 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:01:31 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:02:20 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:00:02 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:02:55 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:09:28 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:05:54 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:03:51 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:06:44 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:08:46 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:05:44 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:02:14 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:04:03 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:04:28 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:02:32 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:01:43 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:04:26 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:12:41 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:01:13 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:00:39 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:00:41 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:01:32 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-18 06:22:35 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.008 |  |
| 2026-04-18 06:02:13 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-04-18 06:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.042 |  |
| 2026-04-18 06:12:03 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.061 |  |
| 2026-04-18 06:05:13 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.065 |  |
| 2026-04-18 06:08:21 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.072 |  |
| 2026-04-18 06:02:32 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.115 |  |
| 2026-04-18 06:03:04 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.162 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)