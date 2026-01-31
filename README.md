# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--01_00:12:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **61,058 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 00:12:22 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:10:51 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:09:53 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:09:49 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-02-01 00:08:45 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 2.571 | 🔺 Rising |
| 2026-02-01 00:08:43 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-02-01 00:08:17 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 2.571 | 🔺 Rising |
| 2026-02-01 00:07:50 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 2.571 | 🔺 Rising |
| 2026-02-01 00:07:08 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:06:20 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-01 00:05:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-01 00:05:55 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.226 |  |
| 2026-02-01 00:05:00 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-02-01 00:04:23 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-02-01 00:04:02 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.228 |  |
| 2026-02-01 00:04:00 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:03:59 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-01 00:03:34 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:03:25 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-02-01 00:03:23 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:03:19 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:02:47 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 00:02:35 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-02-01 00:02:26 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-02-01 00:02:22 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:02:21 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:01:40 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:00:59 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.021 |  |
| 2026-02-01 00:00:26 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:32:21 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:16:24 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 00:08:45 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 2.571 | 🔺 Rising |
| 2026-02-01 00:03:25 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-02-01 00:02:35 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-31 22:26:01 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-01 00:05:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-31 23:01:08 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-01 00:03:59 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-31 23:06:02 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-31 23:00:22 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 00:02:47 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 00:06:20 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-01 00:02:22 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:10:51 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:03:19 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-31 22:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:01:40 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:04:00 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:08:19 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:07:51 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:09:53 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:03:23 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:12:22 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.000 |  |
| 2026-01-31 22:02:37 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:03:34 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:01:40 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:01:52 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:02:21 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:07:08 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:08:43 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-02-01 00:05:00 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-02-01 00:02:26 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-02-01 00:09:49 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-31 22:00:43 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-02-01 00:04:23 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-02-01 00:00:59 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.021 |  |
| 2026-01-31 18:00:08 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | -0.051 |  |
| 2026-01-31 23:10:34 | Manampitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.186 |  |
| 2026-02-01 00:05:55 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.226 |  |
| 2026-02-01 00:04:02 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.228 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)