# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--06_05:04:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **280,158 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 05:04:27 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.092 |  |
| 2026-10-06 05:04:18 | Magura (Kalu Ganga) | 3.12 | 🟢 Normal | -0.423 |  |
| 2026-10-06 05:04:04 | Hanwella (Kelani Ganga) | 4.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-06 05:03:55 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.018 |  |
| 2026-10-06 05:03:53 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 05:03:48 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-10-06 05:03:35 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-06 05:03:19 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-06 05:03:09 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-06 05:02:45 | Giriulla (Maha Oya) | 2.03 | 🟢 Normal | -0.040 |  |
| 2026-10-06 05:02:39 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-06 05:02:37 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-06 05:02:36 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-10-06 05:02:30 | Dunamale (Aththanagalu Oya) | 2.63 | 🟢 Normal | -0.020 |  |
| 2026-10-06 05:02:25 | Glencourse (Kelani Ganga) | 12.30 | 🟢 Normal | -0.220 |  |
| 2026-10-06 05:02:04 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-10-06 05:01:55 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-06 05:01:40 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 05:01:30 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | -0.079 |  |
| 2026-10-06 05:01:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-10-06 05:00:32 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-06 05:00:12 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-06 04:40:11 | Magura (Kalu Ganga) | 3.29 | 🟢 Normal | -0.423 |  |
| 2026-10-06 04:36:50 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.013 |  |
| 2026-10-06 04:28:24 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-06 04:22:18 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 05:01:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-10-06 04:08:07 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-10-06 04:05:03 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-06 05:03:35 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-06 04:07:00 | Panadugama (Nilwala Ganga) | 3.99 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-10-06 05:00:32 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-06 05:04:04 | Hanwella (Kelani Ganga) | 4.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-06 05:02:37 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-06 05:00:12 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-06 05:03:53 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 05:01:40 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 05:01:55 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:04:08 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-06 05:03:09 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-06 05:02:39 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-06 04:06:32 | Rathnapura (Kalu Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:03:21 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-06 04:04:51 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-06 04:28:24 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-06 05:03:19 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-05 18:01:08 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | -0.010 |  |
| 2026-10-06 04:09:14 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-10-06 05:02:04 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-10-06 04:36:50 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.013 |  |
| 2026-10-06 05:03:55 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.018 |  |
| 2026-10-06 05:03:48 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-10-06 05:02:36 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-10-06 05:02:30 | Dunamale (Aththanagalu Oya) | 2.63 | 🟢 Normal | -0.020 |  |
| 2026-10-06 01:03:14 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.022 |  |
| 2026-10-06 04:07:22 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.033 |  |
| 2026-10-06 05:02:45 | Giriulla (Maha Oya) | 2.03 | 🟢 Normal | -0.040 |  |
| 2026-10-06 04:05:05 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.042 |  |
| 2026-10-06 04:00:14 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.050 |  |
| 2026-10-06 04:02:11 | Thawalama (Gin Ganga) | 2.75 | 🟢 Normal | -0.051 |  |
| 2026-10-06 05:01:30 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | -0.079 |  |
| 2026-10-06 04:02:34 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.080 |  |
| 2026-10-06 05:04:27 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.092 |  |
| 2026-10-06 05:02:25 | Glencourse (Kelani Ganga) | 12.30 | 🟢 Normal | -0.220 |  |
| 2026-10-06 05:04:18 | Magura (Kalu Ganga) | 3.12 | 🟢 Normal | -0.423 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)