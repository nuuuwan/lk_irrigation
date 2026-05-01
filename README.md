# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_16:15:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,130 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 16:15:27 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-01 16:12:48 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-01 16:10:58 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 16:10:50 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.186 |  |
| 2026-05-01 16:10:29 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-01 16:10:24 | Glencourse (Kelani Ganga) | 8.00 | 🟢 Normal | -4.669 |  |
| 2026-05-01 16:09:14 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-01 16:08:09 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.037 |  |
| 2026-05-01 16:07:23 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-01 16:07:11 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-05-01 16:07:01 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-01 16:06:51 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.009 |  |
| 2026-05-01 16:06:11 | Thanthirimale (Malwathu Oya) | 2.65 | 🟢 Normal | -0.019 |  |
| 2026-05-01 16:05:45 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-05-01 16:05:07 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 16:04:33 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-01 16:04:30 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-01 16:04:30 | Ellagawa (Kalu Ganga) | 5.04 | 🟢 Normal | -0.059 |  |
| 2026-05-01 16:03:53 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-05-01 16:03:33 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | -0.021 |  |
| 2026-05-01 16:03:29 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-05-01 16:03:27 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-01 16:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-05-01 16:02:53 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | -0.022 |  |
| 2026-05-01 16:02:49 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.039 |  |
| 2026-05-01 16:02:42 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-01 16:02:38 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 16:02:26 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | 0.512 | 🔺 Rising |
| 2026-05-01 16:10:29 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-01 16:07:01 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-01 16:03:27 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-01 16:04:33 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-01 16:04:30 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-01 16:01:35 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-01 16:01:03 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 16:01:35 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-01 16:02:38 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-01 16:12:48 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-01 16:10:58 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 16:09:14 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-01 16:00:50 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-01 16:05:07 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 16:00:35 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-01 16:07:23 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-01 16:02:42 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-01 16:15:27 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-01 16:01:19 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-01 16:06:51 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.009 |  |
| 2026-05-01 16:05:45 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-05-01 16:07:11 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-05-01 16:03:29 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-05-01 16:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-05-01 16:02:30 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-05-01 16:03:53 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-05-01 15:00:08 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -0.014 |  |
| 2026-05-01 16:06:11 | Thanthirimale (Malwathu Oya) | 2.65 | 🟢 Normal | -0.019 |  |
| 2026-05-01 16:00:40 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.020 |  |
| 2026-05-01 16:01:13 | Moragaswewa (Deduru Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-05-01 16:03:33 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | -0.021 |  |
| 2026-05-01 16:02:53 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | -0.022 |  |
| 2026-05-01 16:01:24 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.031 |  |
| 2026-05-01 16:08:09 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.037 |  |
| 2026-05-01 16:02:49 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.039 |  |
| 2026-05-01 16:04:30 | Ellagawa (Kalu Ganga) | 5.04 | 🟢 Normal | -0.059 |  |
| 2026-05-01 16:10:50 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.186 |  |
| 2026-05-01 16:10:24 | Glencourse (Kelani Ganga) | 8.00 | 🟢 Normal | -4.669 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)