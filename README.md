# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--06_22:34:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **280,835 measurements** from **39** stations.
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
| 2026-10-06 22:34:00 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2026-10-06 22:20:24 | Magura (Kalu Ganga) | 2.12 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-06 22:19:47 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:11:33 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:10:47 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-06 22:07:59 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-10-06 22:07:43 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-06 22:07:14 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-10-06 22:07:06 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.030 |  |
| 2026-10-06 22:05:51 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-06 22:05:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.38 | 🟢 Normal | -0.021 |  |
| 2026-10-06 22:05:32 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:05:21 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:05:01 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:04:40 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.031 |  |
| 2026-10-06 22:04:28 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.020 |  |
| 2026-10-06 22:03:57 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:03:55 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:03:37 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:03:34 | Ellagawa (Kalu Ganga) | 5.67 | 🟢 Normal | -0.032 |  |
| 2026-10-06 22:03:27 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | -0.120 |  |
| 2026-10-06 22:02:40 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-06 22:02:39 | Siyambalanduwa (Heda Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:02:32 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-10-06 22:02:24 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 22:02:23 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:02:18 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-06 22:02:11 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.010 |  |
| 2026-10-06 22:02:09 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:01:43 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-06 22:01:21 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 22:01:12 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 22:01:05 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:00:49 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-06 22:00:39 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:00:36 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 22:07:59 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-10-06 22:02:32 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-10-06 22:07:14 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-10-06 22:00:49 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-06 22:02:18 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-06 22:07:43 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-06 22:01:43 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-06 22:05:51 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-06 22:20:24 | Magura (Kalu Ganga) | 2.12 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-06 22:10:47 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-06 22:02:40 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-06 21:03:28 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-06 22:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 22:01:12 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 22:02:24 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 22:19:47 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:03:57 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:02:23 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:01:21 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:05:21 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:00:39 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:03:52 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:11:33 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:01:05 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:00:36 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:02:39 | Siyambalanduwa (Heda Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:02:09 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:03:37 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:01:28 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:05:32 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:02:11 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.010 |  |
| 2026-10-06 18:01:43 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.011 |  |
| 2026-10-06 22:04:28 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.020 |  |
| 2026-10-06 22:05:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.38 | 🟢 Normal | -0.021 |  |
| 2026-10-06 22:34:00 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2026-10-06 22:07:06 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.030 |  |
| 2026-10-06 22:04:40 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.031 |  |
| 2026-10-06 22:03:34 | Ellagawa (Kalu Ganga) | 5.67 | 🟢 Normal | -0.032 |  |
| 2026-10-06 22:03:27 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)