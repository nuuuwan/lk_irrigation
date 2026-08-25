# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_08:14:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **242,896 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 08:14:40 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-25 08:14:23 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.025 |  |
| 2026-08-25 08:10:31 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:08:34 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:07:36 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-25 08:07:01 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-08-25 08:06:10 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-25 08:05:52 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:05:23 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:05:15 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:04:55 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:04:30 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-25 08:04:14 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-08-25 08:04:08 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 08:04:05 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.025 |  |
| 2026-08-25 08:03:57 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:03:53 | Horowpothana (Yan Oya) | 1.91 | 🟢 Normal | -0.011 |  |
| 2026-08-25 08:03:50 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 08:03:38 | Thanthirimale (Malwathu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:03:33 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-08-25 08:03:22 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.104 |  |
| 2026-08-25 08:03:16 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 08:03:12 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:03:06 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:02:52 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.060 |  |
| 2026-08-25 08:02:47 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:02:38 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-25 08:02:23 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:02:14 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:02:03 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 08:01:48 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-08-25 08:03:33 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-08-25 08:04:14 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-08-25 08:02:38 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-25 08:07:36 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-25 08:04:30 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-25 08:06:10 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-25 08:01:31 | Nagalagam Street (Kelani Ganga) | 0.23 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-25 08:03:50 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 08:03:16 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 08:04:08 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 08:14:40 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-25 08:00:54 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:01:16 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:01:40 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:02:14 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:10:31 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:02:52 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:05:23 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:04:55 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:08:34 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:02:23 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:05:15 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:03:12 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:01:33 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:03:57 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:03:06 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:05:52 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:03:38 | Thanthirimale (Malwathu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:02:03 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:02:47 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 08:03:53 | Horowpothana (Yan Oya) | 1.91 | 🟢 Normal | -0.011 |  |
| 2026-08-25 08:00:26 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.013 |  |
| 2026-08-25 08:07:01 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-08-25 08:14:23 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.025 |  |
| 2026-08-25 08:04:05 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.025 |  |
| 2026-08-25 08:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.060 |  |
| 2026-08-25 08:00:33 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.071 |  |
| 2026-08-25 08:03:22 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.104 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)