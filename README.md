# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_15:21:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **243,176 measurements** from **39** stations.
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
| 2026-08-25 15:21:29 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:15:27 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:15:25 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:08:15 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-25 15:07:58 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:07:51 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-25 15:07:50 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.019 |  |
| 2026-08-25 15:07:19 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 15:07:07 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-25 15:07:00 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | -0.039 |  |
| 2026-08-25 15:06:48 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:06:22 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-25 15:06:00 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:05:14 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:05:12 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:04:59 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:04:41 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-25 15:04:39 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:04:30 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:04:20 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 15:03:58 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 15:03:57 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:03:38 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-25 15:03:26 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 15:03:09 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-08-25 15:03:02 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-08-25 15:02:58 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:02:51 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:02:41 | Thanthirimale (Malwathu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:02:32 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:02:26 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2026-08-25 15:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-25 15:02:20 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:02:01 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 15:02:00 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:01:45 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:01:40 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:01:37 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-25 15:00:48 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:00:28 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:00:19 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.080 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 15:07:07 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-25 15:03:09 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-08-25 15:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-25 15:07:51 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-25 15:04:41 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-25 15:03:38 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-25 15:01:37 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-25 15:06:22 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-25 15:03:26 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 15:04:20 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 15:02:01 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 15:03:58 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 15:07:19 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 14:11:46 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 15:08:15 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-25 15:04:39 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:00:28 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:06:48 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:01:45 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:02:58 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:00:48 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:04:30 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:01:40 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:02:00 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:03:57 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:02:32 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:02:20 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:02:51 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:21:29 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:05:14 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:02:41 | Thanthirimale (Malwathu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:07:58 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:05:12 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:15:27 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-25 15:07:50 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.019 |  |
| 2026-08-25 15:03:02 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-08-25 15:02:26 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2026-08-25 15:07:00 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | -0.039 |  |
| 2026-08-25 15:00:19 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)