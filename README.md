# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_04:22:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **229,323 measurements** from **39** stations.
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
| 2026-08-10 04:22:28 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | -0.007 |  |
| 2026-08-10 04:16:07 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:13:15 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-10 04:12:25 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:10:04 | Peradeniya (Mahaweli Ganga) | 3.77 | 🟢 Normal | -0.009 |  |
| 2026-08-10 04:08:42 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.023 |  |
| 2026-08-10 04:08:05 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-10 04:07:53 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.028 |  |
| 2026-08-10 04:06:43 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:06:10 | Ellagawa (Kalu Ganga) | 6.24 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-08-10 04:06:07 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-08-10 04:05:32 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:05:16 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:03:51 | Nawalapitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.029 |  |
| 2026-08-10 04:03:44 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:03:21 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:03:01 | Rathnapura (Kalu Ganga) | 3.04 | 🟢 Normal | -0.064 |  |
| 2026-08-10 04:02:58 | Kithulgala (Kelani Ganga) | 2.31 | 🟢 Normal | -0.054 |  |
| 2026-08-10 04:02:56 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:02:36 | Hanwella (Kelani Ganga) | 2.21 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-10 04:02:16 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:02:08 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:01:42 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:01:21 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:01:12 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-10 04:01:06 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:00:51 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:00:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | -0.073 |  |
| 2026-08-10 04:00:47 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-08-10 04:00:46 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:59:59 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 04:06:10 | Ellagawa (Kalu Ganga) | 6.24 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-08-10 03:06:25 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-10 03:11:49 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-10 04:08:05 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-10 03:06:39 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-10 03:08:25 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-10 03:59:59 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-10 04:01:12 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-10 04:13:15 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-10 04:02:36 | Hanwella (Kelani Ganga) | 2.21 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-09 18:01:36 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 04:02:16 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:00:51 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:01:06 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:01:42 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:01:21 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:03:43 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:02:56 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:12:25 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:03:44 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:06:43 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:05:16 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:00:46 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:05:32 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:02:08 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:16:07 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:03:21 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:07:45 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:22:28 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | -0.007 |  |
| 2026-08-10 04:10:04 | Peradeniya (Mahaweli Ganga) | 3.77 | 🟢 Normal | -0.009 |  |
| 2026-08-10 04:00:47 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-08-10 04:06:07 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-08-10 04:08:42 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.023 |  |
| 2026-08-10 04:07:53 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.028 |  |
| 2026-08-10 04:03:51 | Nawalapitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.029 |  |
| 2026-08-09 18:02:25 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.040 |  |
| 2026-08-10 04:02:58 | Kithulgala (Kelani Ganga) | 2.31 | 🟢 Normal | -0.054 |  |
| 2026-08-10 04:03:01 | Rathnapura (Kalu Ganga) | 3.04 | 🟢 Normal | -0.064 |  |
| 2026-08-10 04:00:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | -0.073 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)