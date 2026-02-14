# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--14_13:18:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **72,862 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 13:18:46 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:17:47 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:14:19 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:11:27 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-14 13:10:15 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:08:02 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:06:52 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:06:35 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:06:21 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:05:58 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | -0.010 |  |
| 2026-02-14 13:05:39 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | -0.067 |  |
| 2026-02-14 13:05:29 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-02-14 13:05:28 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:05:25 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-14 13:05:04 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-02-14 13:04:46 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-14 13:04:38 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:04:10 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-02-14 13:03:51 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:03:51 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-14 13:03:46 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-02-14 13:03:26 | Weraganthota (Mahaweli Ganga) | -2.27 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-14 13:03:17 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:03:07 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:02:54 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:02:49 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:02:34 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:02:18 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-14 13:02:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:02:08 | Padiyathalawa (Maduru Oya) | 2.79 | 🟢 Normal | 1.598 | 🔺 Rising |
| 2026-02-14 13:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.040 |  |
| 2026-02-14 13:02:01 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-02-14 13:01:55 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:01:27 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.054 |  |
| 2026-02-14 13:01:11 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-02-14 13:01:06 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:00:59 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-02-14 13:00:50 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:00:17 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:00:11 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 13:02:08 | Padiyathalawa (Maduru Oya) | 2.79 | 🟢 Normal | 1.598 | 🔺 Rising |
| 2026-02-14 13:05:04 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-02-14 13:04:10 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-02-14 13:02:18 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-14 13:03:26 | Weraganthota (Mahaweli Ganga) | -2.27 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-14 13:05:25 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-14 13:04:46 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-14 13:11:27 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-14 13:01:06 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:03:07 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:00:17 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:18:46 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:06:21 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:01:55 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:06:52 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:05:28 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:02:34 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:02:49 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:02:54 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:08:02 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:03:51 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:00:50 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:02:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:04:38 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:10:15 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:00:11 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:14:19 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:03:17 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:06:35 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-14 13:05:58 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | -0.010 |  |
| 2026-02-14 13:03:51 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-14 13:00:59 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-02-14 13:01:11 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-02-14 13:05:29 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-02-14 13:02:01 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-02-14 13:03:46 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-02-14 13:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.040 |  |
| 2026-02-14 13:01:27 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.054 |  |
| 2026-02-14 13:05:39 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | -0.067 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)