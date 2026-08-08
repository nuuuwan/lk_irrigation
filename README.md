# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_07:41:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **227,635 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 07:41:34 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-08 07:35:28 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:27:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.014 |  |
| 2026-08-08 07:19:08 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:16:57 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-08 07:16:12 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:13:55 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-08 07:11:38 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-08 07:10:20 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-08 07:10:17 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:10:01 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:09:20 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:09:17 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:07:42 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | -0.002 |  |
| 2026-08-08 07:06:51 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:06:48 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-08-08 07:04:46 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-08-08 07:04:22 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:04:01 | Kithulgala (Kelani Ganga) | 2.41 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-08 07:03:59 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 07:03:57 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-08-08 07:03:53 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.029 |  |
| 2026-08-08 07:03:36 | Peradeniya (Mahaweli Ganga) | 3.69 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:03:35 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | -0.010 |  |
| 2026-08-08 07:03:27 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-08-08 07:03:21 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:03:14 | Hanwella (Kelani Ganga) | 2.39 | 🟢 Normal | -0.023 |  |
| 2026-08-08 07:02:59 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:02:51 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:02:14 | Ellagawa (Kalu Ganga) | 5.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 07:02:08 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-08 07:02:08 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.010 |  |
| 2026-08-08 07:02:03 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:02:01 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:01:31 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:00:55 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:00:42 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:00:13 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:00:10 | Nawalapitiya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 07:13:55 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-08 07:04:01 | Kithulgala (Kelani Ganga) | 2.41 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-08 07:41:34 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-08 07:02:08 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-08 07:11:38 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-08 07:02:14 | Ellagawa (Kalu Ganga) | 5.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 07:03:59 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 07:10:20 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-08 07:16:57 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-08 07:03:21 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:10:17 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:19:08 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:02:01 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:04:22 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:01:31 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:16:12 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:02:59 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 06:04:39 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:02:03 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:09:17 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:06:51 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:00:42 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-08 06:01:41 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:03:36 | Peradeniya (Mahaweli Ganga) | 3.69 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:09:20 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:35:28 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:10:01 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:00:55 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 07:07:42 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | -0.002 |  |
| 2026-08-08 07:03:35 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | -0.010 |  |
| 2026-08-08 07:03:57 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-08-08 07:02:08 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.010 |  |
| 2026-08-08 07:04:46 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-08-08 07:03:27 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-08-08 07:27:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.014 |  |
| 2026-08-08 07:06:48 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-08-08 07:00:10 | Nawalapitiya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-08-08 07:03:14 | Hanwella (Kelani Ganga) | 2.39 | 🟢 Normal | -0.023 |  |
| 2026-08-08 07:03:53 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.029 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)