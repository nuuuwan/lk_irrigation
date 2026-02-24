# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--24_10:18:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **81,690 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 10:18:33 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.016 |  |
| 2026-02-24 10:17:29 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.120 |  |
| 2026-02-24 10:15:10 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.009 |  |
| 2026-02-24 10:08:40 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-02-24 10:08:28 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.028 |  |
| 2026-02-24 10:07:49 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.038 |  |
| 2026-02-24 10:07:49 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-24 10:07:20 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-02-24 10:06:26 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:06:20 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:06:09 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:06:05 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | -0.030 |  |
| 2026-02-24 10:05:53 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:05:42 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.019 |  |
| 2026-02-24 10:05:26 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:04:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.030 |  |
| 2026-02-24 10:04:30 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.072 |  |
| 2026-02-24 10:04:15 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-02-24 10:03:48 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.096 |  |
| 2026-02-24 10:03:44 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:03:24 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 10:03:15 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 10:03:07 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:02:58 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:02:57 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | -0.021 |  |
| 2026-02-24 10:02:47 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-02-24 10:02:38 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:02:34 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:02:28 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:02:20 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:02:16 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 10:02:16 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:01:50 | Manampitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-24 10:01:46 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:01:44 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.011 |  |
| 2026-02-24 10:01:35 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:00:34 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.032 |  |
| 2026-02-24 10:00:14 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.221 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 10:00:14 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-02-24 10:01:50 | Manampitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-24 10:02:16 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 10:03:15 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 10:03:24 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 10:07:49 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-24 10:02:34 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:05:53 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:01:46 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:03:07 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:02:38 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:05:26 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:02:16 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:03:44 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:02:20 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:01:35 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:02:28 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:06:20 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:06:26 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:06:09 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:02:58 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-02-24 10:15:10 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.009 |  |
| 2026-02-24 10:08:40 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-02-24 10:04:15 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-02-24 10:07:20 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-02-24 10:01:44 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.011 |  |
| 2026-02-24 09:03:32 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | -0.013 |  |
| 2026-02-24 10:18:33 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.016 |  |
| 2026-02-24 10:05:42 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.019 |  |
| 2026-02-24 10:02:47 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-02-24 10:02:57 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | -0.021 |  |
| 2026-02-24 10:08:28 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.028 |  |
| 2026-02-24 10:04:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.030 |  |
| 2026-02-24 10:06:05 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | -0.030 |  |
| 2026-02-24 10:00:34 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.032 |  |
| 2026-02-24 10:07:49 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.038 |  |
| 2026-02-24 10:04:30 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.072 |  |
| 2026-02-24 10:03:48 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.096 |  |
| 2026-02-24 10:17:29 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)