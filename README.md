# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--16_23:11:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **262,853 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 23:11:08 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-09-16 23:08:32 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-09-16 23:06:12 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.009 |  |
| 2026-09-16 23:05:39 | Baddegama (Gin Ganga) | 3.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-16 23:05:21 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-16 23:05:18 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-16 23:05:10 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-09-16 23:03:46 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | -0.074 |  |
| 2026-09-16 23:03:42 | Glencourse (Kelani Ganga) | 10.07 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-16 23:03:40 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-09-16 23:03:35 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-16 23:03:32 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-16 23:03:31 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-16 23:03:25 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-16 23:03:19 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 23:03:07 | Magura (Kalu Ganga) | 3.24 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-16 23:02:38 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-16 23:02:32 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-16 23:02:24 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | -0.080 |  |
| 2026-09-16 23:02:24 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-16 23:02:12 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.024 |  |
| 2026-09-16 23:02:12 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-16 23:02:10 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-09-16 23:02:10 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.051 |  |
| 2026-09-16 23:01:59 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 23:01:59 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-16 23:01:45 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | -0.053 |  |
| 2026-09-16 23:01:42 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2026-09-16 23:01:32 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-09-16 23:01:06 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-16 23:00:58 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 23:00:47 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-16 23:00:23 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 23:02:24 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-16 23:02:12 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-16 23:03:07 | Magura (Kalu Ganga) | 3.24 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-16 22:05:30 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-16 23:02:10 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-09-16 23:03:25 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-16 23:05:39 | Baddegama (Gin Ganga) | 3.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-16 23:03:42 | Glencourse (Kelani Ganga) | 10.07 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-16 23:11:08 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-09-16 23:05:18 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-16 23:00:58 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 23:03:19 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 18:02:49 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-09-16 23:05:21 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-16 23:03:32 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-16 23:01:59 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 23:03:35 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-16 23:00:47 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:01:06 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-16 23:02:38 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-16 23:00:23 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-16 23:01:06 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-16 22:01:17 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-16 23:03:31 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-16 23:03:40 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-09-16 23:01:59 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-16 22:02:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-09-16 23:06:12 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.009 |  |
| 2026-09-16 23:05:10 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-09-16 23:01:32 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-09-16 18:00:42 | Thanthirimale (Malwathu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-09-16 23:01:42 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2026-09-16 22:07:58 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.012 |  |
| 2026-09-16 23:08:32 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-09-16 23:02:12 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.024 |  |
| 2026-09-16 23:02:10 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.051 |  |
| 2026-09-16 23:01:45 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | -0.053 |  |
| 2026-09-16 23:03:46 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | -0.074 |  |
| 2026-09-16 23:02:24 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)