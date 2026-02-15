# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--15_20:15:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **74,014 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 20:15:30 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.016 |  |
| 2026-02-15 20:14:06 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:12:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:12:38 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-15 20:11:29 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-02-15 20:08:27 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | -0.009 |  |
| 2026-02-15 20:08:18 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:07:12 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:07:04 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-02-15 20:06:25 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.563 |  |
| 2026-02-15 20:05:39 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:05:26 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:05:21 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.563 |  |
| 2026-02-15 20:05:14 | Padiyathalawa (Maduru Oya) | 1.12 | 🟢 Normal | -0.029 |  |
| 2026-02-15 20:05:13 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:05:11 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | -0.019 |  |
| 2026-02-15 20:05:04 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:04:58 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 20:04:08 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.089 |  |
| 2026-02-15 20:03:51 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:03:20 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:03:12 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.021 |  |
| 2026-02-15 20:02:59 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:02:45 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.021 |  |
| 2026-02-15 20:02:44 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:02:42 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:02:27 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:02:23 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:02:22 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:02:15 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:01:56 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:01:35 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:01:19 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.010 |  |
| 2026-02-15 20:01:10 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-02-15 20:00:44 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:00:35 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:00:35 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:00:01 | Manampitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.061 |  |
| 2026-02-15 19:34:27 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 20:12:38 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-15 20:04:58 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 20:05:13 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:02:27 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:01:35 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:00:35 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:01:56 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:02:44 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:02:48 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:03:20 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:02:22 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:02:59 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:07:12 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:05:39 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:02:42 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:03:51 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:05:26 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:02:15 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:05:04 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:08:18 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:01:14 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:14:06 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:00:44 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:12:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-15 20:08:27 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | -0.009 |  |
| 2026-02-15 19:01:49 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-02-15 20:01:19 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.010 |  |
| 2026-02-15 20:15:30 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.016 |  |
| 2026-02-15 20:11:29 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-02-15 20:05:11 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | -0.019 |  |
| 2026-02-15 20:07:04 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-02-15 20:01:10 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-02-15 20:03:12 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.021 |  |
| 2026-02-15 20:02:45 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.021 |  |
| 2026-02-15 20:05:14 | Padiyathalawa (Maduru Oya) | 1.12 | 🟢 Normal | -0.029 |  |
| 2026-02-15 20:00:01 | Manampitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.061 |  |
| 2026-02-15 18:00:16 | Weraganthota (Mahaweli Ganga) | -2.47 | 🟢 Normal | -0.064 |  |
| 2026-02-15 20:04:08 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.089 |  |
| 2026-02-15 20:06:25 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.563 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)