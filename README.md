# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--24_01:05:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **296,236 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 01:05:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.54 | 🟢 Normal | -0.028 |  |
| 2026-10-24 01:05:15 | Putupaula (Kalu Ganga) | 1.85 | 🟢 Normal | -0.021 |  |
| 2026-10-24 01:04:33 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | -0.084 |  |
| 2026-10-24 01:04:05 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-24 01:03:54 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.039 |  |
| 2026-10-24 01:03:38 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.021 |  |
| 2026-10-24 01:03:12 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-10-24 01:03:08 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | -0.020 |  |
| 2026-10-24 01:02:52 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 01:02:49 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-24 01:02:33 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | -0.029 |  |
| 2026-10-24 01:02:31 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-10-24 01:02:29 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-10-24 01:02:23 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 01:02:16 | Hanwella (Kelani Ganga) | 3.57 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-24 01:02:02 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-24 01:01:57 | Ellagawa (Kalu Ganga) | 6.92 | 🟢 Normal | -0.077 |  |
| 2026-10-24 01:01:48 | Moragaswewa (Deduru Oya) | 3.89 | 🟢 Normal | -0.070 |  |
| 2026-10-24 01:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.030 |  |
| 2026-10-24 01:01:29 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-24 01:01:18 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-24 01:00:58 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 00:06:22 | Glencourse (Kelani Ganga) | 11.27 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-10-24 01:02:02 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-24 01:02:16 | Hanwella (Kelani Ganga) | 3.57 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-24 01:00:58 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-24 01:02:52 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 00:00:42 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 01:02:23 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 01:02:49 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-24 01:01:29 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-24 00:11:13 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-24 01:04:05 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-24 01:01:18 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-24 00:14:03 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-10-24 00:02:58 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-23 18:01:50 | Thanthirimale (Malwathu Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-10-24 00:03:58 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-24 01:02:29 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-10-24 01:03:08 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | -0.020 |  |
| 2026-10-24 01:03:12 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-10-24 01:02:31 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-10-24 00:04:07 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.021 |  |
| 2026-10-24 01:03:38 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.021 |  |
| 2026-10-24 01:05:15 | Putupaula (Kalu Ganga) | 1.85 | 🟢 Normal | -0.021 |  |
| 2026-10-24 01:05:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.54 | 🟢 Normal | -0.028 |  |
| 2026-10-24 01:02:33 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | -0.029 |  |
| 2026-10-24 01:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.030 |  |
| 2026-10-24 00:11:07 | Baddegama (Gin Ganga) | 1.93 | 🟢 Normal | -0.031 |  |
| 2026-10-24 00:03:01 | Dunamale (Aththanagalu Oya) | 2.23 | 🟢 Normal | -0.032 |  |
| 2026-10-24 01:03:54 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.039 |  |
| 2026-10-24 00:04:49 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.045 |  |
| 2026-10-23 18:05:52 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | -0.048 |  |
| 2026-10-24 00:14:24 | Rathnapura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.057 |  |
| 2026-10-24 01:01:48 | Moragaswewa (Deduru Oya) | 3.89 | 🟢 Normal | -0.070 |  |
| 2026-10-24 00:06:37 | Panadugama (Nilwala Ganga) | 4.02 | 🟢 Normal | -0.076 |  |
| 2026-10-24 01:01:57 | Ellagawa (Kalu Ganga) | 6.92 | 🟢 Normal | -0.077 |  |
| 2026-10-24 01:04:33 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | -0.084 |  |
| 2026-10-23 20:01:32 | Padiyathalawa (Maduru Oya) | 1.22 | 🟢 Normal | -0.234 |  |
| 2026-10-24 00:05:36 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | -0.416 |  |
| 2026-10-23 18:03:29 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -6.108 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)