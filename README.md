# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--24_20:10:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **82,073 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 20:10:15 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:08:51 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:08:04 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.013 |  |
| 2026-02-24 20:07:05 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:06:49 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-02-24 20:06:40 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:06:33 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-24 20:05:46 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.019 |  |
| 2026-02-24 20:05:43 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-24 20:05:23 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.067 |  |
| 2026-02-24 20:04:48 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-02-24 20:04:20 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.010 |  |
| 2026-02-24 20:04:16 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.029 |  |
| 2026-02-24 20:03:58 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.031 |  |
| 2026-02-24 20:03:57 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:03:54 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-24 20:03:43 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:03:31 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-24 20:03:26 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:03:09 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:02:38 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | -0.010 |  |
| 2026-02-24 20:02:30 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:02:25 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-24 20:02:20 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-02-24 20:02:12 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-02-24 20:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | -0.052 |  |
| 2026-02-24 20:02:07 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.091 |  |
| 2026-02-24 20:01:57 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:01:50 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:01:35 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-02-24 20:01:16 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | -0.030 |  |
| 2026-02-24 20:01:14 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:01:12 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:00:33 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:00:17 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-02-24 19:27:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | -0.052 |  |
| 2026-02-24 19:21:14 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 20:02:25 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-24 20:06:33 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-24 20:03:31 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-24 20:05:43 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-24 19:07:09 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-24 20:03:54 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-24 20:01:57 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:01:50 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:01:12 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:07:05 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:03:16 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:03:09 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:03:43 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:00:33 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:03:57 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:02:30 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:03:26 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:10:15 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:06:40 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:08:51 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:01:14 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-02-24 20:06:49 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-02-24 20:04:20 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.010 |  |
| 2026-02-24 20:02:38 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | -0.010 |  |
| 2026-02-24 20:02:12 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-02-24 20:00:17 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-02-24 20:01:35 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-02-24 20:02:20 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-02-24 20:08:04 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.013 |  |
| 2026-02-24 20:05:46 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.019 |  |
| 2026-02-24 20:04:48 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-02-24 20:04:16 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.029 |  |
| 2026-02-24 20:01:16 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | -0.030 |  |
| 2026-02-24 18:01:47 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-02-24 20:03:58 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.031 |  |
| 2026-02-24 18:06:10 | Weraganthota (Mahaweli Ganga) | -2.27 | 🟢 Normal | -0.045 |  |
| 2026-02-24 20:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | -0.052 |  |
| 2026-02-24 20:05:23 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.067 |  |
| 2026-02-24 20:02:07 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)