# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_06:17:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **196,775 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 06:17:09 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-07-04 06:14:56 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-07-04 06:14:06 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:12:16 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:10:45 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 06:09:34 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:06:53 | Peradeniya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.154 |  |
| 2026-07-04 06:05:23 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-07-04 06:05:13 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-07-04 06:05:03 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-04 06:04:57 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:04:57 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:04:41 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:04:33 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-04 06:03:53 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:03:45 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:03:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.52 | 🟢 Normal | -0.108 |  |
| 2026-07-04 06:03:37 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-04 06:03:28 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:03:27 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-04 06:03:26 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-07-04 06:03:09 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.013 |  |
| 2026-07-04 06:03:04 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-07-04 06:03:02 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-07-04 06:02:35 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:02:27 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 06:02:21 | Hanwella (Kelani Ganga) | 1.60 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-07-04 06:02:13 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:02:11 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:01:51 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.021 |  |
| 2026-07-04 06:01:48 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 06:01:11 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.097 |  |
| 2026-07-04 06:01:10 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:01:08 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:00:47 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:00:38 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-04 06:00:31 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.093 |  |
| 2026-07-04 06:00:19 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.148 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 06:05:13 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-07-04 06:03:26 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-07-04 06:00:19 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-07-04 06:02:21 | Hanwella (Kelani Ganga) | 1.60 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-07-04 06:03:02 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-07-04 06:03:04 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-07-04 06:03:27 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-04 06:05:03 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-04 06:04:33 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-04 06:03:37 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-04 06:14:56 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-07-04 06:05:23 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-07-04 06:17:09 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-07-04 06:00:38 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-04 06:02:27 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 06:01:48 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 06:10:45 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 06:00:47 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:02:13 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:03:28 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:03:45 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:09:34 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:03:53 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:01:08 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:04:57 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:14:06 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:02:11 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:04:41 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:02:35 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:47:16 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:04:57 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-04 06:01:10 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:09:47 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.005 |  |
| 2026-07-04 06:03:09 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.013 |  |
| 2026-07-04 06:01:51 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.021 |  |
| 2026-07-04 06:00:31 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.093 |  |
| 2026-07-04 06:01:11 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.097 |  |
| 2026-07-04 06:03:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.52 | 🟢 Normal | -0.108 |  |
| 2026-07-04 06:06:53 | Peradeniya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.154 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)