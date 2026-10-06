# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--06_18:09:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **280,690 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 18:09:07 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:08:34 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:07:33 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-06 18:07:00 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:05:37 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:05:37 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | -0.040 |  |
| 2026-10-06 18:05:16 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | -0.067 |  |
| 2026-10-06 18:05:09 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-06 18:04:30 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:04:25 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:04:06 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-06 18:04:05 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:03:52 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:03:36 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-06 18:03:34 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.050 |  |
| 2026-10-06 18:03:03 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:03:02 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-10-06 18:03:01 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.058 |  |
| 2026-10-06 18:02:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:02:58 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.066 |  |
| 2026-10-06 18:02:50 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | -0.031 |  |
| 2026-10-06 18:02:47 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | -0.035 |  |
| 2026-10-06 18:02:26 | Panadugama (Nilwala Ganga) | 3.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 18:02:25 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:02:24 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:02:23 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:02:09 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-10-06 18:01:52 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-06 18:01:46 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:01:45 | Glencourse (Kelani Ganga) | 11.04 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:01:43 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.011 |  |
| 2026-10-06 18:01:36 | Glencourse (Kelani Ganga) | 11.04 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:01:28 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:01:25 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-06 18:01:20 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:01:07 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.030 |  |
| 2026-10-06 18:01:06 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:01:00 | Siyambalanduwa (Heda Oya) | 0.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-06 18:00:58 | Dunamale (Aththanagalu Oya) | 2.18 | 🟢 Normal | -0.025 |  |
| 2026-10-06 18:00:53 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-10-06 18:00:37 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-10-06 18:00:13 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-10-06 18:00:09 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 18:04:06 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-06 18:01:52 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-06 18:01:25 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-06 18:07:33 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-06 18:03:36 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-06 18:05:09 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-06 18:01:00 | Siyambalanduwa (Heda Oya) | 0.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-06 18:02:26 | Panadugama (Nilwala Ganga) | 3.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 18:04:30 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:01:20 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:03:52 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:05:37 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:04:25 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:01:45 | Glencourse (Kelani Ganga) | 11.04 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:03:03 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:01:06 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:04:05 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:01:28 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:09:07 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:07:00 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:01:46 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:02:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:03:02 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-10-06 18:00:37 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-10-06 18:00:53 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-10-06 18:00:13 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-10-06 18:01:43 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.011 |  |
| 2026-10-06 18:00:58 | Dunamale (Aththanagalu Oya) | 2.18 | 🟢 Normal | -0.025 |  |
| 2026-10-06 18:02:09 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-10-06 18:01:07 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.030 |  |
| 2026-10-06 18:02:50 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | -0.031 |  |
| 2026-10-06 18:00:09 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.032 |  |
| 2026-10-06 18:02:47 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | -0.035 |  |
| 2026-10-06 18:05:37 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | -0.040 |  |
| 2026-10-06 18:03:34 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.050 |  |
| 2026-10-06 18:03:01 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.058 |  |
| 2026-10-06 18:02:58 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.066 |  |
| 2026-10-06 18:05:16 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | -0.067 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)