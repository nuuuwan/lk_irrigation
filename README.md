# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_17:27:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **113,409 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-01 17:27:08 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | -0.007 |  |
| 2026-04-01 17:17:09 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:09:14 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.134 |  |
| 2026-04-01 17:08:41 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | -36.000 |  |
| 2026-04-01 17:08:40 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | -36.000 |  |
| 2026-04-01 17:08:02 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:07:17 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.134 |  |
| 2026-04-01 17:06:35 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-01 17:06:15 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-04-01 17:06:06 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:06:01 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.026 |  |
| 2026-04-01 17:05:59 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:05:46 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:05:44 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.019 |  |
| 2026-04-01 17:04:26 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:03:52 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:03:42 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:03:36 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-04-01 17:03:36 | Glencourse (Kelani Ganga) | 8.21 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-01 17:03:33 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-04-01 17:03:23 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:03:11 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-04-01 17:03:02 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:02:31 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:02:29 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.098 |  |
| 2026-04-01 17:02:27 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:02:22 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-04-01 17:02:14 | Rathnapura (Kalu Ganga) | 0.29 | 🟢 Normal | -0.012 |  |
| 2026-04-01 17:02:13 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:02:12 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-04-01 17:02:12 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-04-01 17:02:08 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-01 17:01:56 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | -0.010 |  |
| 2026-04-01 17:01:29 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-04-01 17:01:16 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:01:10 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-04-01 17:01:09 | Pitabeddara (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:56:57 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.022 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-01 17:03:36 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-04-01 17:06:35 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-01 17:03:36 | Glencourse (Kelani Ganga) | 8.21 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-01 16:56:57 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-01 17:03:42 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:01:16 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-01 16:02:15 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:02:31 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:17:09 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:05:59 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:01:09 | Pitabeddara (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:03:23 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:06:06 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:04:26 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:02:27 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:02:13 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:05:46 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:03:02 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:03:52 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:08:02 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:02:12 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-01 17:27:08 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | -0.007 |  |
| 2026-04-01 17:06:15 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-04-01 17:02:12 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-04-01 17:01:56 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | -0.010 |  |
| 2026-04-01 17:03:11 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-04-01 17:03:33 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-04-01 17:02:08 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-01 17:01:10 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-04-01 17:01:29 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-04-01 17:02:22 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-04-01 17:02:14 | Rathnapura (Kalu Ganga) | 0.29 | 🟢 Normal | -0.012 |  |
| 2026-04-01 17:05:44 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.019 |  |
| 2026-04-01 17:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-04-01 17:06:01 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.026 |  |
| 2026-04-01 17:02:29 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.098 |  |
| 2026-04-01 17:07:17 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.134 |  |
| 2026-04-01 17:09:14 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.134 |  |
| 2026-04-01 17:08:41 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)