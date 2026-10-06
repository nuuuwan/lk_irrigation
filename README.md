# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--06_17:07:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **280,641 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 17:07:14 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.058 |  |
| 2026-10-06 17:07:12 | Ellagawa (Kalu Ganga) | 5.68 | 🟢 Normal | -0.055 |  |
| 2026-10-06 17:06:25 | Siyambalanduwa (Heda Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-06 17:06:22 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.011 |  |
| 2026-10-06 17:05:50 | Peradeniya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.019 |  |
| 2026-10-06 17:05:38 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.154 |  |
| 2026-10-06 17:05:21 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.040 |  |
| 2026-10-06 17:05:17 | Panadugama (Nilwala Ganga) | 3.55 | 🟢 Normal | -0.030 |  |
| 2026-10-06 17:05:16 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-10-06 17:05:14 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | -0.019 |  |
| 2026-10-06 17:04:53 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.042 |  |
| 2026-10-06 17:04:06 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-06 17:03:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | -0.050 |  |
| 2026-10-06 17:03:49 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-06 17:03:22 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-06 17:03:09 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.024 |  |
| 2026-10-06 17:03:03 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-06 17:03:01 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.080 |  |
| 2026-10-06 17:02:29 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.092 |  |
| 2026-10-06 17:02:29 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-10-06 17:02:23 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.019 |  |
| 2026-10-06 17:02:18 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-10-06 17:02:18 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | -0.010 |  |
| 2026-10-06 17:02:07 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 17:02:06 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 17:01:59 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 17:01:31 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-06 17:01:26 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.012 |  |
| 2026-10-06 17:01:24 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-10-06 17:01:21 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-06 17:01:08 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-06 17:00:58 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-06 17:00:58 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-06 17:00:53 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.012 |  |
| 2026-10-06 17:00:26 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-06 16:31:53 | Thanthirimale (Malwathu Oya) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 17:01:31 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-06 17:02:29 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-10-06 17:00:26 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-06 17:03:22 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-06 17:01:08 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-06 17:02:06 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 16:11:14 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-06 17:04:06 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-06 17:01:59 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 17:00:58 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-06 16:02:29 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-06 17:03:03 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-06 17:06:25 | Siyambalanduwa (Heda Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-06 17:02:07 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 17:03:49 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-06 17:01:21 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-06 17:02:18 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-10-06 17:01:24 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-10-06 17:00:58 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-06 17:05:16 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-10-06 17:02:18 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | -0.010 |  |
| 2026-10-06 17:06:22 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.011 |  |
| 2026-10-06 17:01:26 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.012 |  |
| 2026-10-06 17:00:53 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.012 |  |
| 2026-10-06 17:05:50 | Peradeniya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.019 |  |
| 2026-10-06 17:05:14 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | -0.019 |  |
| 2026-10-06 17:02:23 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.019 |  |
| 2026-10-06 17:03:09 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.024 |  |
| 2026-10-06 17:05:17 | Panadugama (Nilwala Ganga) | 3.55 | 🟢 Normal | -0.030 |  |
| 2026-10-06 16:09:39 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | -0.037 |  |
| 2026-10-06 16:07:34 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.039 |  |
| 2026-10-06 17:05:21 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.040 |  |
| 2026-10-06 17:04:53 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.042 |  |
| 2026-10-06 17:03:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | -0.050 |  |
| 2026-10-06 17:07:12 | Ellagawa (Kalu Ganga) | 5.68 | 🟢 Normal | -0.055 |  |
| 2026-10-06 17:07:14 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.058 |  |
| 2026-10-06 17:03:01 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.080 |  |
| 2026-10-06 17:02:29 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.092 |  |
| 2026-10-06 17:05:38 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.154 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)