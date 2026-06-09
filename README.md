# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--09_06:32:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **174,429 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 06:32:37 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | -0.001 |  |
| 2026-06-09 06:24:29 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:21:19 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-09 06:09:13 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:09:09 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | -0.135 |  |
| 2026-06-09 06:08:33 | Hanwella (Kelani Ganga) | 3.60 | 🟢 Normal | -0.028 |  |
| 2026-06-09 06:08:32 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:06:59 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:06:25 | Ellagawa (Kalu Ganga) | 6.38 | 🟢 Normal | -0.020 |  |
| 2026-06-09 06:06:20 | Dunamale (Aththanagalu Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:06:19 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.065 |  |
| 2026-06-09 06:05:47 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:05:33 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:05:17 | Deraniyagala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-09 06:04:48 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | -0.101 |  |
| 2026-06-09 06:04:24 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:04:19 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-09 06:04:14 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.019 |  |
| 2026-06-09 06:04:05 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.023 |  |
| 2026-06-09 06:03:27 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:03:24 | Putupaula (Kalu Ganga) | 1.69 | 🟢 Normal | -0.020 |  |
| 2026-06-09 06:03:06 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:03:05 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-06-09 06:02:56 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | -0.078 |  |
| 2026-06-09 06:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.18 | 🟢 Normal | -0.099 |  |
| 2026-06-09 06:02:37 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-09 06:02:35 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:02:13 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | -0.012 |  |
| 2026-06-09 06:02:10 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:01:51 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:01:49 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:01:46 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-06-09 06:01:15 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 06:01:13 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 06:00:56 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:00:30 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.036 |  |
| 2026-06-09 06:00:19 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.037 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 06:01:46 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-06-09 06:04:19 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-08 18:00:59 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-09 06:05:17 | Deraniyagala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-09 06:02:37 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-09 06:01:15 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 06:01:13 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 06:21:19 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-09 06:24:29 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:05:47 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:00:56 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:04:24 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:01:49 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:06:59 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:09:13 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:05:33 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:08:32 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:02:35 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:06:20 | Dunamale (Aththanagalu Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:02:10 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:01:51 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:03:27 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:03:06 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-09 06:32:37 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | -0.001 |  |
| 2026-06-09 06:03:05 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-06-09 06:02:13 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | -0.012 |  |
| 2026-06-09 05:33:59 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.014 |  |
| 2026-06-09 06:04:14 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.019 |  |
| 2026-06-09 06:06:25 | Ellagawa (Kalu Ganga) | 6.38 | 🟢 Normal | -0.020 |  |
| 2026-06-09 06:03:24 | Putupaula (Kalu Ganga) | 1.69 | 🟢 Normal | -0.020 |  |
| 2026-06-09 06:04:05 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.023 |  |
| 2026-06-09 06:08:33 | Hanwella (Kelani Ganga) | 3.60 | 🟢 Normal | -0.028 |  |
| 2026-06-09 06:00:30 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.036 |  |
| 2026-06-09 06:00:19 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.037 |  |
| 2026-06-09 06:06:19 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.065 |  |
| 2026-06-09 06:02:56 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | -0.078 |  |
| 2026-06-09 06:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.18 | 🟢 Normal | -0.099 |  |
| 2026-06-09 06:04:48 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | -0.101 |  |
| 2026-06-09 06:09:09 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | -0.135 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)