# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--09_10:13:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **174,587 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 10:13:21 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.027 |  |
| 2026-06-09 10:10:12 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:09:20 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | -0.020 |  |
| 2026-06-09 10:08:38 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:07:35 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-06-09 10:07:22 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-09 10:07:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.09 | 🟢 Normal | -0.009 |  |
| 2026-06-09 10:07:03 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-09 10:06:35 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:05:38 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | -0.010 |  |
| 2026-06-09 10:05:34 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | -0.019 |  |
| 2026-06-09 10:05:33 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:04:54 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-06-09 10:04:38 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-06-09 10:04:27 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:04:10 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 10:03:48 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:03:45 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:03:32 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:03:31 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.049 |  |
| 2026-06-09 10:03:29 | Hanwella (Kelani Ganga) | 3.40 | 🟢 Normal | -0.050 |  |
| 2026-06-09 10:03:20 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-06-09 10:03:10 | Ellagawa (Kalu Ganga) | 6.24 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-09 10:02:46 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:02:42 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:02:41 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-06-09 10:02:33 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.012 |  |
| 2026-06-09 10:02:29 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:02:08 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.031 |  |
| 2026-06-09 10:02:03 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 10:02:00 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.010 |  |
| 2026-06-09 10:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-06-09 10:01:44 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-06-09 10:01:28 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:00:46 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:00:43 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:00:16 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:00:16 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 10:07:35 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-06-09 10:03:10 | Ellagawa (Kalu Ganga) | 6.24 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-09 10:07:03 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-09 10:04:10 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 10:02:03 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 10:00:16 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:01:28 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:04:22 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:04:27 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:00:43 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:03:45 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:03:48 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:03:32 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:06:35 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:02:46 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:02:29 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:08:38 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:05:33 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:10:12 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:00:46 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:00:16 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:02:42 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-09 10:07:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.09 | 🟢 Normal | -0.009 |  |
| 2026-06-09 10:07:22 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-09 10:02:00 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.010 |  |
| 2026-06-09 10:05:38 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | -0.010 |  |
| 2026-06-09 10:04:54 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-06-09 10:04:38 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-06-09 10:02:41 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-06-09 10:02:33 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.012 |  |
| 2026-06-09 10:05:34 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | -0.019 |  |
| 2026-06-09 10:09:20 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | -0.020 |  |
| 2026-06-09 10:03:20 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-06-09 10:01:44 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-06-09 10:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-06-09 10:13:21 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.027 |  |
| 2026-06-09 10:02:08 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.031 |  |
| 2026-06-09 10:03:31 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.049 |  |
| 2026-06-09 10:03:29 | Hanwella (Kelani Ganga) | 3.40 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)