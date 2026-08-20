# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_19:26:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **238,852 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 19:26:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-08-20 19:15:05 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:10:22 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.098 |  |
| 2026-08-20 19:09:22 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-08-20 19:07:25 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:06:39 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 19:06:38 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:06:20 | Rathnapura (Kalu Ganga) | 2.91 | 🟢 Normal | -0.104 |  |
| 2026-08-20 19:06:10 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:06:05 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-20 19:05:28 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | -0.010 |  |
| 2026-08-20 19:05:06 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:05:04 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:04:33 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.037 |  |
| 2026-08-20 19:04:25 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-08-20 19:04:24 | Ellagawa (Kalu Ganga) | 6.23 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-08-20 19:04:04 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:03:59 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-08-20 19:03:46 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-08-20 19:03:32 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-08-20 19:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:03:03 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-20 19:02:39 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:02:24 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:02:21 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.033 |  |
| 2026-08-20 19:02:19 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.030 |  |
| 2026-08-20 19:01:59 | Thanamalwila (Kirindi Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:01:49 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:01:44 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:01:43 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-08-20 19:01:41 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:01:35 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:01:19 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:01:13 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:00:16 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 19:03:32 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-08-20 19:03:59 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-08-20 19:04:24 | Ellagawa (Kalu Ganga) | 6.23 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-08-20 19:03:03 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-20 19:06:05 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-20 19:04:25 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-08-20 19:06:39 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 19:26:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-08-20 18:02:56 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:01:35 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:00:16 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:01:44 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:01:49 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:04:04 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:01:19 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-20 18:04:45 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:15:05 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:05:04 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:02:24 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:02:39 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:01:41 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:07:25 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:05:06 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:06:10 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-20 18:02:19 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:06:38 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:01:13 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:01:59 | Thanamalwila (Kirindi Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-20 19:09:22 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-08-20 19:05:28 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | -0.010 |  |
| 2026-08-20 19:03:46 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-08-20 19:01:43 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-08-20 18:01:53 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-08-20 19:02:19 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.030 |  |
| 2026-08-20 19:02:21 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.033 |  |
| 2026-08-20 19:04:33 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.037 |  |
| 2026-08-20 19:10:22 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.098 |  |
| 2026-08-20 19:06:20 | Rathnapura (Kalu Ganga) | 2.91 | 🟢 Normal | -0.104 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)