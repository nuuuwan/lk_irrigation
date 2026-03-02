# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--02_14:14:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **87,227 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 14:14:32 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:12:48 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:10:20 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-03-02 14:09:58 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:09:36 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:07:41 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:06:29 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.022 |  |
| 2026-03-02 14:06:28 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-03-02 14:06:14 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.047 |  |
| 2026-03-02 14:06:12 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:05:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.019 |  |
| 2026-03-02 14:05:34 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.279 |  |
| 2026-03-02 14:05:11 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-03-02 14:04:10 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-02 14:03:53 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-03-02 14:03:32 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-03-02 14:03:27 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:03:25 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.279 |  |
| 2026-03-02 14:03:17 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-03-02 14:03:08 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | -0.010 |  |
| 2026-03-02 14:02:47 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:02:46 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:02:34 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-02 14:02:33 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | -0.040 |  |
| 2026-03-02 14:02:27 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:02:21 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:02:01 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-02 14:01:59 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:01:42 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:01:42 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:01:40 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:01:33 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-02 14:01:23 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | -0.181 |  |
| 2026-03-02 14:01:22 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:01:15 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | -0.057 |  |
| 2026-03-02 14:01:13 | Horowpothana (Yan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:01:04 | Thanthirimale (Malwathu Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-03-02 14:00:55 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:00:23 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:26:50 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.277 |  |
| 2026-03-02 13:24:40 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.277 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 14:02:34 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-02 14:04:10 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-02 14:10:20 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-03-02 14:02:01 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-02 14:01:33 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-02 14:01:59 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:00:23 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:02:47 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:00:55 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:01:42 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:02:21 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:01:13 | Horowpothana (Yan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:07:41 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:06:12 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:12:48 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:03:27 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:01:42 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:14:32 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:02:46 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:01:40 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:09:36 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:09:58 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:10:09 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:01:22 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-02 14:05:11 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-03-02 14:03:53 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-03-02 14:03:08 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | -0.010 |  |
| 2026-03-02 14:03:32 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-03-02 14:06:28 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-03-02 14:01:04 | Thanthirimale (Malwathu Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-03-02 14:05:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.019 |  |
| 2026-03-02 14:03:17 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-03-02 14:06:29 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.022 |  |
| 2026-03-02 14:02:33 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | -0.040 |  |
| 2026-03-02 14:06:14 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.047 |  |
| 2026-03-02 14:01:15 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | -0.057 |  |
| 2026-03-02 14:01:23 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | -0.181 |  |
| 2026-03-02 13:26:50 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.277 |  |
| 2026-03-02 14:05:34 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.279 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)