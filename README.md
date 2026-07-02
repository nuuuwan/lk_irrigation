# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--02_06:12:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **194,983 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-02 06:12:23 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-02 06:08:13 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-07-02 06:07:18 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-07-02 06:06:44 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:06:20 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | -0.011 |  |
| 2026-07-02 06:06:08 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-07-02 06:05:14 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.111 |  |
| 2026-07-02 06:04:49 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.023 |  |
| 2026-07-02 06:04:47 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-07-02 06:04:43 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | -0.040 |  |
| 2026-07-02 06:04:39 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:04:35 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:04:18 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:04:18 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.012 |  |
| 2026-07-02 06:03:57 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:03:54 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:03:40 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.118 |  |
| 2026-07-02 06:03:24 | Glencourse (Kelani Ganga) | 9.88 | 🟢 Normal | -0.351 |  |
| 2026-07-02 06:03:21 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-07-02 06:03:05 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-07-02 06:03:05 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:03:03 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-02 06:02:42 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:02:30 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-02 06:02:16 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.030 |  |
| 2026-07-02 06:02:05 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:01:29 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:01:28 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-07-02 06:01:28 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:01:27 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:01:19 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-07-02 06:01:18 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:01:15 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:01:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.71 | 🟢 Normal | -0.103 |  |
| 2026-07-02 06:00:52 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:00:49 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.042 |  |
| 2026-07-02 06:00:35 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-02 06:01:19 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-07-02 06:08:13 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-07-02 06:01:28 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-07-02 06:02:30 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-02 06:03:03 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-02 06:12:23 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-02 06:02:42 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:01:29 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:01:18 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:01:27 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:04:35 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:06:53 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:06:44 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:14:49 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:03:54 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:00:52 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:00:35 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:02:05 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:04:39 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:01:15 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:04:10 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:02:02 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:03:05 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:01:28 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-02 06:06:08 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-07-02 06:03:05 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-07-02 06:03:21 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-07-02 06:04:47 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-07-02 06:06:20 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | -0.011 |  |
| 2026-07-02 06:04:18 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.012 |  |
| 2026-07-02 06:07:18 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-07-02 06:04:49 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.023 |  |
| 2026-07-02 06:02:16 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.030 |  |
| 2026-07-02 06:04:43 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | -0.040 |  |
| 2026-07-02 06:00:49 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.042 |  |
| 2026-07-02 06:01:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.71 | 🟢 Normal | -0.103 |  |
| 2026-07-02 06:05:14 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.111 |  |
| 2026-07-02 06:03:40 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.118 |  |
| 2026-07-02 06:03:24 | Glencourse (Kelani Ganga) | 9.88 | 🟢 Normal | -0.351 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)