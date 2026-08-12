# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_05:21:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **231,161 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 05:21:08 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-12 05:14:02 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-12 05:12:41 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-12 05:09:20 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-12 05:09:16 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.053 |  |
| 2026-08-12 05:09:09 | Glencourse (Kelani Ganga) | 10.51 | 🟢 Normal | 0.000 |  |
| 2026-08-12 05:08:58 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-08-12 05:08:06 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-12 05:07:54 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-08-12 05:07:11 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-08-12 05:06:40 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -0.013 |  |
| 2026-08-12 05:06:39 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-08-12 05:06:33 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.093 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 00:01:58 | Weraganthota (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.541 | 🔺 Rising |
| 2026-08-12 05:01:00 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-12 05:02:43 | Hanwella (Kelani Ganga) | 1.89 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-12 05:02:41 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 05:02:48 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 05:04:34 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-12 05:06:01 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-12 05:00:56 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-12 05:21:08 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-12 05:01:35 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-12 05:03:46 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-12 05:03:01 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-11 18:15:33 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-12 05:08:06 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-12 04:02:54 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-12 05:01:47 | Ellagawa (Kalu Ganga) | 5.14 | 🟢 Normal | 0.000 |  |
| 2026-08-12 05:09:20 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:01:40 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-12 05:09:09 | Glencourse (Kelani Ganga) | 10.51 | 🟢 Normal | 0.000 |  |
| 2026-08-12 05:02:27 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-12 05:12:41 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-12 05:05:57 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-08-12 05:00:32 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-11 18:01:06 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-12 05:14:02 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-12 04:01:58 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-12 05:03:02 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-08-12 05:07:11 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-08-12 05:02:38 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-08-12 05:06:39 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-08-12 05:03:38 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.011 |  |
| 2026-08-12 05:06:40 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -0.013 |  |
| 2026-08-12 05:04:20 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.019 |  |
| 2026-08-12 05:08:58 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-08-12 05:07:54 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-08-12 04:07:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.023 |  |
| 2026-08-12 05:05:15 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.041 |  |
| 2026-08-12 05:09:16 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.053 |  |
| 2026-08-12 05:06:33 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)