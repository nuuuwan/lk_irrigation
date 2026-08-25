# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_11:19:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **243,018 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 11:19:24 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:17:15 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:15:40 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:15:18 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-25 11:14:25 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.027 |  |
| 2026-08-25 11:14:13 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:12:17 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.120 |  |
| 2026-08-25 11:11:18 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.203 |  |
| 2026-08-25 11:10:54 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:08:17 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:07:55 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 11:07:46 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 11:06:20 | Thanthirimale (Malwathu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:06:16 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:05:37 | Glencourse (Kelani Ganga) | 9.56 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-25 11:05:35 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:05:06 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-08-25 11:04:54 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:04:52 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:04:07 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:04:04 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.59 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-08-25 11:03:58 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 11:03:54 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:03:48 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-08-25 11:03:26 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-08-25 11:03:22 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -1.000 |  |
| 2026-08-25 11:03:03 | Ellagawa (Kalu Ganga) | 4.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-25 11:03:01 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:02:51 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-25 11:02:46 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -1.000 |  |
| 2026-08-25 11:02:16 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-08-25 11:02:07 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:01:46 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:01:46 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.012 |  |
| 2026-08-25 11:01:39 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:01:28 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.049 |  |
| 2026-08-25 11:01:19 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.010 |  |
| 2026-08-25 11:01:02 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:00:37 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:00:07 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 11:02:51 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-25 11:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.59 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-08-25 11:03:48 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-08-25 11:05:37 | Glencourse (Kelani Ganga) | 9.56 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-25 11:03:03 | Ellagawa (Kalu Ganga) | 4.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-25 11:03:58 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 11:07:46 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 11:07:55 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 11:15:18 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-25 11:03:54 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:00:07 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:05:35 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:17:15 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:14:13 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:01:46 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:01:02 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:03:01 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:15:40 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:04:07 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:04:52 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:00:37 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:04:04 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:04:54 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:06:16 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:10:54 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:06:20 | Thanthirimale (Malwathu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:19:24 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:08:17 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:01:39 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:03:26 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-08-25 11:01:19 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.010 |  |
| 2026-08-25 11:05:06 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-08-25 11:01:46 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.012 |  |
| 2026-08-25 11:02:16 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-08-25 11:14:25 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.027 |  |
| 2026-08-25 11:01:28 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.049 |  |
| 2026-08-25 11:12:17 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.120 |  |
| 2026-08-25 11:11:18 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.203 |  |
| 2026-08-25 11:03:22 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -1.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)