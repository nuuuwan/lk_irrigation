# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--24_00:14:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **296,214 measurements** from **39** stations.
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
| 2026-10-24 00:14:24 | Rathnapura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.057 |  |
| 2026-10-24 00:14:03 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-10-24 00:11:13 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-24 00:11:07 | Baddegama (Gin Ganga) | 1.93 | 🟢 Normal | -0.031 |  |
| 2026-10-24 00:08:03 | Putupaula (Kalu Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-10-24 00:07:25 | Ellagawa (Kalu Ganga) | 6.99 | 🟢 Normal | -0.082 |  |
| 2026-10-24 00:07:22 | Hanwella (Kelani Ganga) | 3.54 | 🟢 Normal | -0.019 |  |
| 2026-10-24 00:07:11 | Kithulgala (Kelani Ganga) | 2.27 | 🟢 Normal | -0.059 |  |
| 2026-10-24 00:06:37 | Panadugama (Nilwala Ganga) | 4.02 | 🟢 Normal | -0.076 |  |
| 2026-10-24 00:06:22 | Glencourse (Kelani Ganga) | 11.27 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-10-24 00:06:01 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -72.000 |  |
| 2026-10-24 00:05:59 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -72.000 |  |
| 2026-10-24 00:05:38 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-24 00:05:36 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | -0.416 |  |
| 2026-10-24 00:05:06 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-24 00:05:04 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-24 00:04:49 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.045 |  |
| 2026-10-24 00:04:07 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.021 |  |
| 2026-10-24 00:03:58 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-24 00:03:54 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-24 00:03:01 | Dunamale (Aththanagalu Oya) | 2.23 | 🟢 Normal | -0.032 |  |
| 2026-10-24 00:02:58 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-24 00:02:54 | Deraniyagala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.030 |  |
| 2026-10-24 00:02:30 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-10-24 00:02:17 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.050 |  |
| 2026-10-24 00:02:13 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | -0.031 |  |
| 2026-10-24 00:01:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.57 | 🟢 Normal | -0.034 |  |
| 2026-10-24 00:01:34 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-24 00:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.050 |  |
| 2026-10-24 00:01:29 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 00:01:15 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-24 00:00:42 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 00:00:30 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-10-24 00:00:10 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-24 00:00:09 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.030 |  |
| 2026-10-23 23:54:03 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | -0.416 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 00:00:30 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-10-24 00:06:22 | Glencourse (Kelani Ganga) | 11.27 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-10-24 00:03:54 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-24 00:00:42 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 00:01:29 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 00:00:10 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-24 00:01:34 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-24 00:01:15 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-24 00:11:13 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-24 00:05:04 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-24 00:05:38 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-24 00:05:06 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-24 00:14:03 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-10-24 00:02:58 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-24 00:08:03 | Putupaula (Kalu Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-10-23 18:01:50 | Thanthirimale (Malwathu Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-10-24 00:03:58 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-24 00:07:22 | Hanwella (Kelani Ganga) | 3.54 | 🟢 Normal | -0.019 |  |
| 2026-10-24 00:02:30 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-10-24 00:04:07 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.021 |  |
| 2026-10-24 00:02:54 | Deraniyagala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.030 |  |
| 2026-10-24 00:00:09 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.030 |  |
| 2026-10-24 00:11:07 | Baddegama (Gin Ganga) | 1.93 | 🟢 Normal | -0.031 |  |
| 2026-10-24 00:02:13 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | -0.031 |  |
| 2026-10-24 00:03:01 | Dunamale (Aththanagalu Oya) | 2.23 | 🟢 Normal | -0.032 |  |
| 2026-10-24 00:01:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.57 | 🟢 Normal | -0.034 |  |
| 2026-10-24 00:04:49 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.045 |  |
| 2026-10-23 18:05:52 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | -0.048 |  |
| 2026-10-24 00:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.050 |  |
| 2026-10-24 00:02:17 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.050 |  |
| 2026-10-24 00:14:24 | Rathnapura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.057 |  |
| 2026-10-24 00:07:11 | Kithulgala (Kelani Ganga) | 2.27 | 🟢 Normal | -0.059 |  |
| 2026-10-24 00:06:37 | Panadugama (Nilwala Ganga) | 4.02 | 🟢 Normal | -0.076 |  |
| 2026-10-24 00:07:25 | Ellagawa (Kalu Ganga) | 6.99 | 🟢 Normal | -0.082 |  |
| 2026-10-23 23:01:48 | Moragaswewa (Deduru Oya) | 4.03 | 🟢 Normal | -0.084 |  |
| 2026-10-23 20:01:32 | Padiyathalawa (Maduru Oya) | 1.22 | 🟢 Normal | -0.234 |  |
| 2026-10-24 00:05:36 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | -0.416 |  |
| 2026-10-23 18:03:29 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -6.108 |  |
| 2026-10-24 00:06:01 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)