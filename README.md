# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--11_14:11:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **285,015 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 14:11:46 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-11 14:11:18 | Rathnapura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.073 |  |
| 2026-10-11 14:07:23 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 14:07:20 | Peradeniya (Mahaweli Ganga) | 2.49 | 🟢 Normal | -0.010 |  |
| 2026-10-11 14:07:00 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.012 |  |
| 2026-10-11 14:06:57 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | -0.019 |  |
| 2026-10-11 14:06:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.38 | 🟢 Normal | -0.029 |  |
| 2026-10-11 14:06:34 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-10-11 14:05:49 | Ellagawa (Kalu Ganga) | 6.45 | 🟢 Normal | -0.085 |  |
| 2026-10-11 14:05:21 | Giriulla (Maha Oya) | 2.33 | 🟢 Normal | -0.067 |  |
| 2026-10-11 14:05:21 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-10-11 14:05:17 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-11 14:04:57 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-10-11 14:04:35 | Badalgama (Maha Oya) | 3.61 | 🟢 Normal | -0.068 |  |
| 2026-10-11 14:04:22 | Hanwella (Kelani Ganga) | 2.84 | 🟢 Normal | -0.020 |  |
| 2026-10-11 14:04:17 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-11 14:04:11 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-11 14:03:57 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 14:03:55 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.052 |  |
| 2026-10-11 14:03:47 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-11 14:03:36 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-10-11 14:03:20 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.020 |  |
| 2026-10-11 14:02:51 | Dunamale (Aththanagalu Oya) | 2.66 | 🟢 Normal | -0.089 |  |
| 2026-10-11 14:02:35 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 14:02:34 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-11 14:02:31 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.019 |  |
| 2026-10-11 14:02:30 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal | -0.067 |  |
| 2026-10-11 14:02:21 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-10-11 14:02:13 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | -0.011 |  |
| 2026-10-11 14:02:03 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.032 |  |
| 2026-10-11 14:02:02 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-11 14:01:57 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.034 |  |
| 2026-10-11 14:01:28 | Moragaswewa (Deduru Oya) | 2.64 | 🟢 Normal | -0.021 |  |
| 2026-10-11 14:01:19 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-10-11 14:01:07 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.051 |  |
| 2026-10-11 14:00:51 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-11 14:00:10 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 14:03:36 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-10-11 14:05:17 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-11 14:02:35 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 14:03:57 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 14:03:47 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-11 14:04:17 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-11 14:11:46 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-11 14:06:34 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-10-11 14:07:23 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 14:04:11 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-11 14:02:34 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:02:58 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-11 14:00:51 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-11 14:00:10 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-11 13:04:25 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-11 14:04:57 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-10-11 14:07:20 | Peradeniya (Mahaweli Ganga) | 2.49 | 🟢 Normal | -0.010 |  |
| 2026-10-11 14:02:13 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | -0.011 |  |
| 2026-10-11 14:07:00 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.012 |  |
| 2026-10-11 14:06:57 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | -0.019 |  |
| 2026-10-11 14:02:31 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.019 |  |
| 2026-10-11 14:02:21 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-10-11 14:04:22 | Hanwella (Kelani Ganga) | 2.84 | 🟢 Normal | -0.020 |  |
| 2026-10-11 14:01:19 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-10-11 14:03:20 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.020 |  |
| 2026-10-11 14:05:21 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-10-11 14:01:28 | Moragaswewa (Deduru Oya) | 2.64 | 🟢 Normal | -0.021 |  |
| 2026-10-11 14:06:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.38 | 🟢 Normal | -0.029 |  |
| 2026-10-11 14:02:03 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.032 |  |
| 2026-10-11 14:01:57 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.034 |  |
| 2026-10-11 14:01:07 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.051 |  |
| 2026-10-11 14:03:55 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.052 |  |
| 2026-10-11 13:12:53 | Magura (Kalu Ganga) | 2.89 | 🟢 Normal | -0.063 |  |
| 2026-10-11 14:02:30 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal | -0.067 |  |
| 2026-10-11 14:05:21 | Giriulla (Maha Oya) | 2.33 | 🟢 Normal | -0.067 |  |
| 2026-10-11 14:04:35 | Badalgama (Maha Oya) | 3.61 | 🟢 Normal | -0.068 |  |
| 2026-10-11 14:11:18 | Rathnapura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.073 |  |
| 2026-10-11 14:05:49 | Ellagawa (Kalu Ganga) | 6.45 | 🟢 Normal | -0.085 |  |
| 2026-10-11 14:02:51 | Dunamale (Aththanagalu Oya) | 2.66 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)