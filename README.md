# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--23_04:26:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **323,262 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 04:26:33 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:17:17 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:10:14 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:10:04 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:08:36 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:06:52 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:06:32 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:05:43 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:05:28 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.129 |  |
| 2026-11-23 04:04:15 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:03:58 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-23 04:03:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.107 |  |
| 2026-11-23 04:03:34 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-11-23 04:03:17 | Moragaswewa (Deduru Oya) | 1.97 | 🟢 Normal | -0.175 |  |
| 2026-11-23 04:03:09 | Manampitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.045 |  |
| 2026-11-23 04:02:03 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-23 04:02:03 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 04:01:43 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:01:28 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.036 |  |
| 2026-11-23 04:01:27 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:01:15 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-11-23 04:01:13 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.195 |  |
| 2026-11-23 04:01:07 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:00:26 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 04:00:22 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-11-23 04:00:12 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:00:07 | Moraketiya (Walawe Ganga) | 2.60 | 🟢 Normal | -0.057 |  |
| 2026-11-23 03:58:06 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 04:03:34 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-11-23 04:03:58 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-23 03:01:13 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-23 03:05:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-23 03:08:23 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-22 18:00:53 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-23 04:02:03 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-23 04:00:26 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 04:02:03 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 04:01:07 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:01:43 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:00:10 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:08:36 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:10:14 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:12:16 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:17:17 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:06:32 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:04:15 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:05:43 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:06:52 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:10:04 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:02:00 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:00:12 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:26:33 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:01:27 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-23 04:00:22 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-11-23 04:01:15 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-11-22 17:02:02 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-23 04:01:28 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.036 |  |
| 2026-11-23 04:03:09 | Manampitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.045 |  |
| 2026-11-23 04:00:07 | Moraketiya (Walawe Ganga) | 2.60 | 🟢 Normal | -0.057 |  |
| 2026-11-23 03:02:59 | Thawalama (Gin Ganga) | 2.87 | 🟢 Normal | -0.082 |  |
| 2026-11-23 03:27:26 | Panadugama (Nilwala Ganga) | 4.20 | 🟢 Normal | -0.084 |  |
| 2026-11-23 03:06:35 | Rathnapura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.106 |  |
| 2026-11-23 04:03:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.107 |  |
| 2026-11-23 04:05:28 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.129 |  |
| 2026-11-23 04:03:17 | Moragaswewa (Deduru Oya) | 1.97 | 🟢 Normal | -0.175 |  |
| 2026-11-23 04:01:13 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.195 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)