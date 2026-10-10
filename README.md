# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--10_13:09:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **284,071 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 13:09:26 | Holombuwa (Kelani Ganga) | 1.13 | 🟢 Normal | -0.029 |  |
| 2026-10-10 13:09:08 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-10 13:08:25 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-10-10 13:07:31 | Dunamale (Aththanagalu Oya) | 3.29 | 🟢 Normal | -0.039 |  |
| 2026-10-10 13:07:08 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-10 13:07:00 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.169 |  |
| 2026-10-10 13:06:58 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | -0.028 |  |
| 2026-10-10 13:06:10 | Nagalagam Street (Kelani Ganga) | 0.84 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-10-10 13:06:03 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-10 13:05:46 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-10 13:05:19 | Badalgama (Maha Oya) | 4.43 | 🟢 Normal | -0.080 |  |
| 2026-10-10 13:05:18 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.031 |  |
| 2026-10-10 13:04:25 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 13:04:02 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | -0.010 |  |
| 2026-10-10 13:04:00 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.019 |  |
| 2026-10-10 13:03:34 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.296 |  |
| 2026-10-10 13:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.63 | 🟢 Normal | -0.030 |  |
| 2026-10-10 13:03:27 | Hanwella (Kelani Ganga) | 3.33 | 🟢 Normal | -0.031 |  |
| 2026-10-10 13:03:16 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-10 13:03:14 | Ellagawa (Kalu Ganga) | 6.98 | 🟢 Normal | -0.020 |  |
| 2026-10-10 13:02:59 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | -0.033 |  |
| 2026-10-10 13:02:50 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-10-10 13:02:46 | Moragaswewa (Deduru Oya) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-10-10 13:02:16 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 13:02:09 | Giriulla (Maha Oya) | 3.30 | 🟢 Normal | -0.100 |  |
| 2026-10-10 13:02:07 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-10 13:01:46 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-10 13:01:16 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.021 |  |
| 2026-10-10 13:01:16 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-10-10 13:01:14 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-10 13:00:39 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-10 13:00:35 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | -0.021 |  |
| 2026-10-10 13:00:30 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.033 |  |
| 2026-10-10 13:00:08 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-10-10 12:36:42 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.006 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 13:08:25 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-10-10 13:06:10 | Nagalagam Street (Kelani Ganga) | 0.84 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-10-10 13:06:03 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-10 13:00:39 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-10 13:03:16 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-10 13:04:25 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 13:01:14 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-10 13:02:16 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 13:01:46 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-10 12:04:09 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-10 13:09:08 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-10 13:02:07 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-10 13:05:46 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-10 13:07:08 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-10 12:36:42 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.006 |  |
| 2026-10-10 13:02:46 | Moragaswewa (Deduru Oya) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-10-10 13:01:16 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-10-10 13:04:02 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | -0.010 |  |
| 2026-10-10 13:00:08 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-10-10 13:02:50 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-10-10 13:04:00 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.019 |  |
| 2026-10-10 13:03:14 | Ellagawa (Kalu Ganga) | 6.98 | 🟢 Normal | -0.020 |  |
| 2026-10-10 12:03:19 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-10-10 13:00:35 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | -0.021 |  |
| 2026-10-10 13:01:16 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.021 |  |
| 2026-10-10 13:06:58 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | -0.028 |  |
| 2026-10-10 13:09:26 | Holombuwa (Kelani Ganga) | 1.13 | 🟢 Normal | -0.029 |  |
| 2026-10-10 13:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.63 | 🟢 Normal | -0.030 |  |
| 2026-10-10 13:03:27 | Hanwella (Kelani Ganga) | 3.33 | 🟢 Normal | -0.031 |  |
| 2026-10-10 13:05:18 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.031 |  |
| 2026-10-10 13:00:30 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.033 |  |
| 2026-10-10 13:02:59 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | -0.033 |  |
| 2026-10-10 13:07:31 | Dunamale (Aththanagalu Oya) | 3.29 | 🟢 Normal | -0.039 |  |
| 2026-10-10 13:05:19 | Badalgama (Maha Oya) | 4.43 | 🟢 Normal | -0.080 |  |
| 2026-10-10 12:04:31 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.087 |  |
| 2026-10-10 13:02:09 | Giriulla (Maha Oya) | 3.30 | 🟢 Normal | -0.100 |  |
| 2026-10-10 12:04:51 | Rathnapura (Kalu Ganga) | 2.63 | 🟢 Normal | -0.129 |  |
| 2026-10-10 13:07:00 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.169 |  |
| 2026-10-10 13:03:34 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.296 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)