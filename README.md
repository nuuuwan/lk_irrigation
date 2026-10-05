# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--05_08:15:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **279,402 measurements** from **39** stations.
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
| 2026-10-05 08:15:00 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.041 |  |
| 2026-10-05 08:14:00 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-05 08:12:00 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.009 |  |
| 2026-10-05 08:10:49 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-05 08:10:47 | Panadugama (Nilwala Ganga) | 3.72 | 🟢 Normal | -0.032 |  |
| 2026-10-05 08:09:49 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-05 08:09:03 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 08:09:02 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-10-05 08:08:14 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-10-05 08:07:02 | Glencourse (Kelani Ganga) | 11.62 | 🟢 Normal | -0.140 |  |
| 2026-10-05 08:06:47 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-05 08:06:13 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -0.070 |  |
| 2026-10-05 08:04:48 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-05 08:04:48 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-05 08:04:33 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-05 08:04:32 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-05 08:04:21 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-10-05 08:04:10 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.026 |  |
| 2026-10-05 08:04:05 | Giriulla (Maha Oya) | 1.97 | 🟢 Normal | -0.079 |  |
| 2026-10-05 08:03:58 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-10-05 08:03:54 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-10-05 08:03:41 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-10-05 08:03:37 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.032 |  |
| 2026-10-05 08:03:22 | Hanwella (Kelani Ganga) | 3.85 | 🟢 Normal | -0.103 |  |
| 2026-10-05 08:03:16 | Ellagawa (Kalu Ganga) | 6.22 | 🟢 Normal | -0.010 |  |
| 2026-10-05 08:02:50 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-10-05 08:02:30 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.032 |  |
| 2026-10-05 08:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.010 |  |
| 2026-10-05 08:02:25 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-10-05 08:02:08 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-05 08:02:06 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.019 |  |
| 2026-10-05 08:01:56 | Dunamale (Aththanagalu Oya) | 2.69 | 🟢 Normal | -0.053 |  |
| 2026-10-05 08:01:54 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.083 |  |
| 2026-10-05 08:01:54 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.020 |  |
| 2026-10-05 08:01:51 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-05 08:01:33 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 08:02:08 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-05 08:04:48 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-05 08:01:51 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-05 08:14:00 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-05 08:01:01 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-05 08:01:33 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 08:09:49 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-05 08:10:49 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-05 08:09:03 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 08:04:33 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-05 08:04:32 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-05 08:06:47 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-05 08:04:48 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-05 08:12:00 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.009 |  |
| 2026-10-05 08:03:41 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-10-05 08:03:54 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-10-05 08:03:58 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-10-05 08:04:21 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-10-05 08:08:14 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-10-05 08:03:16 | Ellagawa (Kalu Ganga) | 6.22 | 🟢 Normal | -0.010 |  |
| 2026-10-05 08:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.010 |  |
| 2026-10-05 08:02:50 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-10-05 08:02:06 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.019 |  |
| 2026-10-05 08:01:54 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.020 |  |
| 2026-10-05 08:09:02 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-10-05 08:02:25 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-10-05 08:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.023 |  |
| 2026-10-05 08:04:10 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.026 |  |
| 2026-10-05 08:03:37 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.032 |  |
| 2026-10-05 08:02:30 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.032 |  |
| 2026-10-05 08:10:47 | Panadugama (Nilwala Ganga) | 3.72 | 🟢 Normal | -0.032 |  |
| 2026-10-05 08:15:00 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.041 |  |
| 2026-10-05 08:01:56 | Dunamale (Aththanagalu Oya) | 2.69 | 🟢 Normal | -0.053 |  |
| 2026-10-05 08:06:13 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -0.070 |  |
| 2026-10-05 08:00:20 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.071 |  |
| 2026-10-05 08:04:05 | Giriulla (Maha Oya) | 1.97 | 🟢 Normal | -0.079 |  |
| 2026-10-05 08:01:54 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.083 |  |
| 2026-10-05 08:03:22 | Hanwella (Kelani Ganga) | 3.85 | 🟢 Normal | -0.103 |  |
| 2026-10-05 08:07:02 | Glencourse (Kelani Ganga) | 11.62 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)