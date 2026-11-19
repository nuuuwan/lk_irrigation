# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--19_13:29:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **320,088 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-19 13:29:31 | Panadugama (Nilwala Ganga) | 1.38 | 🟢 Normal | -1.395 |  |
| 2026-11-19 13:19:15 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:17:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.23 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-19 13:14:06 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:12:07 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-11-19 13:11:32 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.009 |  |
| 2026-11-19 13:10:09 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-11-19 13:09:41 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:08:48 | Moraketiya (Walawe Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:07:33 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:06:19 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.009 |  |
| 2026-11-19 13:05:39 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:05:10 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:05:07 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:04:50 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:04:37 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-11-19 13:04:02 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:03:42 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:03:29 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:03:15 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:03:11 | Hanwella (Kelani Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:02:50 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:02:41 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-11-19 13:02:32 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:02:26 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:02:12 | Katharagama (Menik Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:02:11 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:01:53 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:01:45 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:01:34 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:01:23 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:01:19 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:01:15 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-19 13:01:14 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:00:37 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:00:28 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:00:20 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:00:12 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:00:04 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-19 13:17:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.23 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-19 13:01:15 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-19 13:00:12 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:00:37 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:01:45 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:02:50 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:02:26 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:05:39 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:03:42 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:02:32 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:00:28 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:09:41 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:08:48 | Moraketiya (Walawe Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:04:50 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:01:53 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:01:23 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:05:07 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:14:06 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:19:15 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:01:19 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:11:32 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.009 |  |
| 2026-11-19 13:12:07 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-11-19 13:10:09 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-11-19 13:06:19 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.009 |  |
| 2026-11-19 13:05:10 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:03:15 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:03:29 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:03:11 | Hanwella (Kelani Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:02:11 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:02:12 | Katharagama (Menik Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:04:02 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:07:33 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:01:14 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:01:34 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:00:20 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:02:41 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-11-19 13:04:37 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-11-19 13:29:31 | Panadugama (Nilwala Ganga) | 1.38 | 🟢 Normal | -1.395 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)