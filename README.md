# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--01_18:11:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **194,567 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 18:11:30 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.009 |  |
| 2026-07-01 18:08:56 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:08:23 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:08:00 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-07-01 18:06:53 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:06:19 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.019 |  |
| 2026-07-01 18:05:33 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:05:28 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.019 |  |
| 2026-07-01 18:05:02 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:04:45 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | -0.033 |  |
| 2026-07-01 18:04:29 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:04:02 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 18:03:59 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:03:31 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:03:25 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.030 |  |
| 2026-07-01 18:03:20 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:03:09 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.019 |  |
| 2026-07-01 18:03:09 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:03:08 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 18:03:02 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.120 |  |
| 2026-07-01 18:02:57 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:02:40 | Hanwella (Kelani Ganga) | 1.81 | 🟢 Normal | -0.020 |  |
| 2026-07-01 18:02:37 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 18:02:34 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 18:02:31 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 18:02:29 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:02:25 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:02:15 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | -0.030 |  |
| 2026-07-01 18:02:02 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:01:57 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:01:31 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:01:25 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-07-01 18:01:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:01:12 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-07-01 18:00:24 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:00:10 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-01 17:58:26 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 18:00:10 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-01 18:02:31 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 18:03:08 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 18:02:37 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 18:02:34 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 18:04:02 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 18:02:29 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:02:57 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:03:59 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:01:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:01:57 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:06:53 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:03:20 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:05:33 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:00:24 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:03:31 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:03:09 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:04:29 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:02:25 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:08:56 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:02:02 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:08:23 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-01 17:58:26 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:01:31 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:05:02 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:11:30 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.009 |  |
| 2026-07-01 18:08:00 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-07-01 18:01:25 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-07-01 18:01:12 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-07-01 18:05:28 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.019 |  |
| 2026-07-01 18:06:19 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.019 |  |
| 2026-07-01 18:03:09 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.019 |  |
| 2026-07-01 18:02:40 | Hanwella (Kelani Ganga) | 1.81 | 🟢 Normal | -0.020 |  |
| 2026-07-01 18:03:25 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.030 |  |
| 2026-07-01 18:02:15 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | -0.030 |  |
| 2026-07-01 18:04:45 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | -0.033 |  |
| 2026-07-01 17:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | -0.053 |  |
| 2026-07-01 18:03:02 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)