# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--06_04:02:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,070 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 04:02:56 | Moragaswewa (Deduru Oya) | 2.96 | 🟢 Normal | -0.020 |  |
| 2026-11-06 04:02:27 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-06 04:02:26 | Hanwella (Kelani Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-11-06 04:02:22 | Kuda Oya (Kirindi Oya) | 2.07 | 🟢 Normal | -0.031 |  |
| 2026-11-06 04:02:18 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-06 04:02:15 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.032 |  |
| 2026-11-06 04:02:05 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-06 04:02:02 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 04:01:55 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-11-06 04:01:40 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | -0.051 |  |
| 2026-11-06 04:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-11-06 04:01:15 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-11-06 04:00:40 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-11-06 04:00:23 | Moraketiya (Walawe Ganga) | 1.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-06 04:00:16 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | -0.021 |  |
| 2026-11-06 03:40:06 | Rathnapura (Kalu Ganga) | 2.73 | 🟢 Normal | -0.069 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 03:13:35 | Ellagawa (Kalu Ganga) | 6.15 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-06 04:00:23 | Moraketiya (Walawe Ganga) | 1.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-06 03:06:09 | Putupaula (Kalu Ganga) | 1.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-06 04:02:02 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 03:02:29 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:03:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-06 04:02:05 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-06 04:02:27 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-06 04:02:26 | Hanwella (Kelani Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-11-06 03:06:48 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-06 03:12:50 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-11-06 03:02:59 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-11-06 04:02:18 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-06 03:02:23 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-06 01:03:58 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-06 03:03:35 | Panadugama (Nilwala Ganga) | 4.23 | 🟢 Normal | -0.010 |  |
| 2026-11-06 04:01:55 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-11-06 04:01:15 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-11-06 04:00:40 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-11-06 04:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-11-05 18:01:46 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | -0.012 |  |
| 2026-11-06 03:05:12 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | -0.020 |  |
| 2026-11-06 04:02:56 | Moragaswewa (Deduru Oya) | 2.96 | 🟢 Normal | -0.020 |  |
| 2026-11-06 03:06:57 | Badalgama (Maha Oya) | 3.25 | 🟢 Normal | -0.020 |  |
| 2026-11-06 04:00:16 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | -0.021 |  |
| 2026-11-06 03:06:08 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | -0.022 |  |
| 2026-11-06 03:04:07 | Giriulla (Maha Oya) | 1.91 | 🟢 Normal | -0.030 |  |
| 2026-11-06 04:02:22 | Kuda Oya (Kirindi Oya) | 2.07 | 🟢 Normal | -0.031 |  |
| 2026-11-06 04:02:15 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.032 |  |
| 2026-11-06 03:05:26 | Thanamalwila (Kirindi Oya) | 1.86 | 🟢 Normal | -0.039 |  |
| 2026-11-06 03:01:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.60 | 🟢 Normal | -0.041 |  |
| 2026-11-05 18:01:57 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.049 |  |
| 2026-11-06 04:01:40 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | -0.051 |  |
| 2026-11-06 03:02:17 | Manampitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.052 |  |
| 2026-11-06 03:05:47 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.061 |  |
| 2026-11-06 03:40:06 | Rathnapura (Kalu Ganga) | 2.73 | 🟢 Normal | -0.069 |  |
| 2026-11-06 00:04:54 | Magura (Kalu Ganga) | 2.69 | 🟢 Normal | -0.092 |  |
| 2026-11-06 03:09:11 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.140 |  |
| 2026-11-06 03:07:10 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -1.663 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)