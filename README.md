# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--21_06:16:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **78,814 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 06:16:03 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:13:14 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:12:34 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-21 06:10:52 | Weraganthota (Mahaweli Ganga) | -1.10 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-21 06:10:28 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.058 |  |
| 2026-02-21 06:09:28 | Padiyathalawa (Maduru Oya) | 1.70 | 🟢 Normal | -234.000 |  |
| 2026-02-21 06:09:26 | Padiyathalawa (Maduru Oya) | 1.83 | 🟢 Normal | -234.000 |  |
| 2026-02-21 06:08:24 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 1.422 | 🔺 Rising |
| 2026-02-21 06:07:28 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:07:24 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-21 06:07:10 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:06:41 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:06:29 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-21 06:06:25 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:06:21 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:05:26 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-21 06:05:21 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:05:01 | Padiyathalawa (Maduru Oya) | 1.73 | 🟢 Normal | -234.000 |  |
| 2026-02-21 06:04:38 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.029 |  |
| 2026-02-21 06:04:02 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:03:26 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:03:24 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:03:08 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-02-21 06:03:05 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-02-21 06:02:55 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.021 |  |
| 2026-02-21 06:02:47 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:02:47 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:02:19 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:02:09 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:01:53 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:01:39 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 1.422 | 🔺 Rising |
| 2026-02-21 06:01:36 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | -0.075 |  |
| 2026-02-21 06:01:25 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:01:22 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:01:12 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:01:09 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:01:04 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:00:49 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.041 |  |
| 2026-02-21 06:00:40 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.034 |  |
| 2026-02-21 06:00:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | -0.273 |  |
| 2026-02-21 05:52:59 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-21 05:45:39 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-21 05:27:51 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 06:08:24 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 1.422 | 🔺 Rising |
| 2026-02-21 06:12:34 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-21 06:06:29 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-21 06:03:05 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-02-21 06:05:26 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-21 06:07:24 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-21 06:10:52 | Weraganthota (Mahaweli Ganga) | -1.10 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-21 06:16:03 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:03:24 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:01:22 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:03:26 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:01:25 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-20 18:04:38 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:04:02 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:07:10 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:01:53 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:07:28 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:06:41 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:06:21 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:02:19 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:01:04 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:02:09 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:01:12 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:05:21 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:02:47 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-20 18:01:33 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:13:14 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:01:09 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:06:25 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-21 06:03:08 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-02-21 06:02:55 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.021 |  |
| 2026-02-21 06:04:38 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.029 |  |
| 2026-02-21 06:00:40 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.034 |  |
| 2026-02-21 06:00:49 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.041 |  |
| 2026-02-21 05:00:55 | Manampitiya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.051 |  |
| 2026-02-21 06:10:28 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.058 |  |
| 2026-02-21 06:01:36 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | -0.075 |  |
| 2026-02-21 06:00:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | -0.273 |  |
| 2026-02-21 06:09:28 | Padiyathalawa (Maduru Oya) | 1.70 | 🟢 Normal | -234.000 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)