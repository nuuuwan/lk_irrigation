# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--06_09:09:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **280,332 measurements** from **39** stations.
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
| 2026-10-06 09:09:47 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | -0.051 |  |
| 2026-10-06 09:08:35 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.172 |  |
| 2026-10-06 09:08:00 | Glencourse (Kelani Ganga) | 11.69 | 🟢 Normal | -0.126 |  |
| 2026-10-06 09:06:37 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | -0.020 |  |
| 2026-10-06 09:06:32 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-06 09:06:21 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-10-06 09:06:05 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-10-06 09:05:17 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-06 09:05:07 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-06 09:04:52 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.284 |  |
| 2026-10-06 09:04:52 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 09:04:43 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-06 09:04:42 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.115 |  |
| 2026-10-06 09:04:33 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-06 09:04:24 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-10-06 09:04:16 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | -0.063 |  |
| 2026-10-06 09:04:10 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.021 |  |
| 2026-10-06 09:04:08 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.019 |  |
| 2026-10-06 09:03:53 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.111 |  |
| 2026-10-06 09:03:53 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-06 09:03:52 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-06 09:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 09:03:17 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-10-06 09:03:07 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.021 |  |
| 2026-10-06 09:02:58 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.126 |  |
| 2026-10-06 09:02:43 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-06 09:02:38 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.029 |  |
| 2026-10-06 09:02:18 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-10-06 09:02:14 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | -0.051 |  |
| 2026-10-06 09:02:10 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 09:02:00 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.022 |  |
| 2026-10-06 09:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-10-06 09:01:29 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-06 09:01:17 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 09:01:15 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-06 09:01:14 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-06 09:01:10 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-06 09:00:55 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.051 |  |
| 2026-10-06 09:00:44 | Thanthirimale (Malwathu Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 09:00:13 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.038 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 09:01:14 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-06 09:05:17 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-06 09:00:13 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-06 09:04:43 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-06 09:04:52 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 09:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 09:00:44 | Thanthirimale (Malwathu Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 09:01:29 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-06 09:01:17 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 09:01:10 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-06 09:05:07 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-06 09:03:53 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-06 09:04:33 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-06 09:06:32 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-06 09:01:15 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-06 09:02:10 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 09:06:05 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-10-06 09:02:18 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-10-06 09:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-10-06 09:03:52 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-06 09:06:21 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-10-06 09:03:17 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-10-06 09:04:08 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.019 |  |
| 2026-10-06 09:06:37 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | -0.020 |  |
| 2026-10-06 09:04:24 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-10-06 09:04:10 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.021 |  |
| 2026-10-06 09:03:07 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.021 |  |
| 2026-10-06 09:02:00 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.022 |  |
| 2026-10-06 09:02:38 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.029 |  |
| 2026-10-06 09:02:14 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | -0.051 |  |
| 2026-10-06 09:00:55 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.051 |  |
| 2026-10-06 09:09:47 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | -0.051 |  |
| 2026-10-06 09:04:16 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | -0.063 |  |
| 2026-10-06 09:03:53 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.111 |  |
| 2026-10-06 09:04:42 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.115 |  |
| 2026-10-06 09:08:00 | Glencourse (Kelani Ganga) | 11.69 | 🟢 Normal | -0.126 |  |
| 2026-10-06 09:02:58 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.126 |  |
| 2026-10-06 09:08:35 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.172 |  |
| 2026-10-06 09:04:52 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.284 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)