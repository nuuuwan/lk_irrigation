# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--08_17:23:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **67,648 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 17:23:04 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.008 |  |
| 2026-02-08 17:12:00 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:09:59 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:09:24 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.055 |  |
| 2026-02-08 17:08:59 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.009 |  |
| 2026-02-08 17:08:03 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-08 17:06:27 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:06:26 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-02-08 17:06:20 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:06:02 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:05:52 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.013 |  |
| 2026-02-08 17:05:39 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:05:03 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-08 17:05:01 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.012 |  |
| 2026-02-08 17:05:00 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-02-08 17:04:59 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-02-08 17:04:51 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:04:18 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-02-08 17:03:42 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 17:03:19 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:02:59 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-08 17:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.081 |  |
| 2026-02-08 17:02:44 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:02:39 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.011 |  |
| 2026-02-08 17:02:37 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-02-08 17:02:34 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-02-08 17:02:19 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:02:19 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-08 17:02:13 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:01:53 | Horowpothana (Yan Oya) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-02-08 17:01:42 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:01:39 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-02-08 17:01:23 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:01:20 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-02-08 17:01:08 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:01:05 | Weraganthota (Mahaweli Ganga) | -2.29 | 🟢 Normal | -0.042 |  |
| 2026-02-08 17:00:51 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-02-08 17:00:21 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 17:05:00 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-02-08 17:02:59 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-08 17:05:03 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-08 17:08:03 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-08 17:02:19 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-08 17:03:42 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 15:04:07 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.003 |  |
| 2026-02-08 17:02:19 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:01:23 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:01:42 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:09:59 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:05:39 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:06:02 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:04:51 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:02:44 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:06:20 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:00:21 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:12:00 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:02:13 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:06:27 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:03:19 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:01:08 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 17:23:04 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.008 |  |
| 2026-02-08 17:08:59 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.009 |  |
| 2026-02-08 17:06:26 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-02-08 17:04:59 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-02-08 17:02:37 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-02-08 17:00:51 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-02-08 17:01:39 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-02-08 17:02:39 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.011 |  |
| 2026-02-08 17:05:01 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.012 |  |
| 2026-02-08 17:05:52 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.013 |  |
| 2026-02-08 17:04:18 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-02-08 17:01:53 | Horowpothana (Yan Oya) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-02-08 17:02:34 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-02-08 17:01:20 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-02-08 17:01:05 | Weraganthota (Mahaweli Ganga) | -2.29 | 🟢 Normal | -0.042 |  |
| 2026-02-08 17:09:24 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.055 |  |
| 2026-02-08 17:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)