# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--02_15:10:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **195,331 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-02 15:10:20 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:09:00 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-07-02 15:08:07 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:07:24 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:07:22 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:07:05 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:04:58 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:04:21 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:04:13 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-07-02 15:04:04 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:03:45 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:03:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | -0.030 |  |
| 2026-07-02 15:02:55 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:02:54 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:02:53 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.020 |  |
| 2026-07-02 15:02:49 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-07-02 15:02:43 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-02 15:02:41 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:02:36 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:02:32 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:02:26 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-07-02 15:02:25 | Ellagawa (Kalu Ganga) | 5.12 | 🟢 Normal | -0.010 |  |
| 2026-07-02 15:02:20 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:02:10 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.043 |  |
| 2026-07-02 15:02:02 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:01:53 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-02 15:01:39 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-07-02 15:01:28 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-07-02 15:01:21 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:00:57 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-07-02 15:00:48 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.013 |  |
| 2026-07-02 15:00:25 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.010 |  |
| 2026-07-02 15:00:14 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-02 15:02:26 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-07-02 15:02:43 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-02 14:10:39 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-02 15:01:53 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-02 15:02:41 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:18:07 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:01:21 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:07:22 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:02:36 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:04:58 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:10:20 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:04:04 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:07:24 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:05:51 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:04:21 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:00:14 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:02:32 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:03:45 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:02:20 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:08:07 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:07:05 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:02:02 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:02:54 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:01:45 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:01:28 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-02 15:02:55 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:13:37 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-07-02 15:09:00 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-07-02 15:02:49 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-07-02 15:01:39 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-07-02 15:02:25 | Ellagawa (Kalu Ganga) | 5.12 | 🟢 Normal | -0.010 |  |
| 2026-07-02 15:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-07-02 15:00:25 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.010 |  |
| 2026-07-02 15:00:48 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.013 |  |
| 2026-07-02 15:02:53 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.020 |  |
| 2026-07-02 15:04:13 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-07-02 15:00:57 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-07-02 15:03:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | -0.030 |  |
| 2026-07-02 15:02:10 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.043 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)