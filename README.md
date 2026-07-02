# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--02_14:08:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **195,291 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-02 14:08:43 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:08:28 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.019 |  |
| 2026-07-02 14:07:16 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-07-02 14:07:04 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:06:40 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.028 |  |
| 2026-07-02 14:06:39 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-07-02 14:05:51 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:03:47 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-07-02 14:03:43 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-02 14:03:32 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-07-02 14:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.49 | 🟢 Normal | -0.040 |  |
| 2026-07-02 14:03:28 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-07-02 14:03:04 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:03:02 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:02:59 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:02:57 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:02:28 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-07-02 14:02:25 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:02:23 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | -0.010 |  |
| 2026-07-02 14:02:17 | Ellagawa (Kalu Ganga) | 5.13 | 🟢 Normal | -0.020 |  |
| 2026-07-02 14:02:16 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:01:50 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:01:48 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-02 14:01:47 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-07-02 14:01:45 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:01:40 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:01:27 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.020 |  |
| 2026-07-02 14:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-07-02 14:00:49 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:00:42 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:00:36 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-07-02 14:00:31 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-07-02 13:32:31 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-07-02 13:24:11 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-02 14:01:47 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-07-02 14:03:47 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-07-02 14:03:28 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-07-02 14:01:48 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-02 13:32:31 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-07-02 14:03:43 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-02 13:04:35 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-02 14:01:50 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:00:49 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 13:01:40 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:01:40 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:08:43 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:00:42 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:02:59 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-02 13:11:24 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:05:51 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:03:04 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:02:16 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:02:57 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:07:04 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:03:02 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:02:25 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:01:45 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-02 13:00:34 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-02 14:02:28 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-07-02 14:03:32 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-07-02 14:00:31 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-07-02 14:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-07-02 14:02:23 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | -0.010 |  |
| 2026-07-02 14:00:36 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-07-02 14:06:39 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-07-02 14:08:28 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.019 |  |
| 2026-07-02 14:02:17 | Ellagawa (Kalu Ganga) | 5.13 | 🟢 Normal | -0.020 |  |
| 2026-07-02 14:01:27 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.020 |  |
| 2026-07-02 14:07:16 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-07-02 13:04:53 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-07-02 13:24:11 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.022 |  |
| 2026-07-02 14:06:40 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.028 |  |
| 2026-07-02 14:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.49 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)