# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_11:26:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,827 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 11:26:04 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.016 |  |
| 2026-05-02 11:25:45 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-02 11:25:18 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.008 |  |
| 2026-05-02 11:18:35 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:12:58 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.104 |  |
| 2026-05-02 11:08:58 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.029 |  |
| 2026-05-02 11:07:39 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-05-02 11:06:28 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-05-02 11:05:34 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-05-02 11:05:31 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.021 |  |
| 2026-05-02 11:05:20 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-05-02 11:04:57 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:04:46 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:04:42 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.038 |  |
| 2026-05-02 11:04:40 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:03:54 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 11:03:36 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-02 11:03:18 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | -0.029 |  |
| 2026-05-02 11:03:17 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | -0.021 |  |
| 2026-05-02 11:03:14 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-02 11:03:01 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:03:01 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:02:54 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:02:53 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.023 |  |
| 2026-05-02 11:02:40 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-05-02 11:02:36 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-05-02 11:02:26 | Glencourse (Kelani Ganga) | 8.86 | 🟢 Normal | -0.071 |  |
| 2026-05-02 11:02:17 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.050 |  |
| 2026-05-02 11:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-02 11:01:55 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:01:47 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-05-02 11:01:41 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:01:29 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:01:25 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:01:21 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.023 |  |
| 2026-05-02 11:01:19 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-05-02 11:01:17 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.010 |  |
| 2026-05-02 11:00:28 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:00:17 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 11:02:40 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-05-02 11:05:20 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-05-02 11:02:36 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-05-02 11:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-02 11:25:45 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-02 11:03:54 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 11:01:25 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:00:28 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:18:35 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:01:55 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:03:01 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:04:40 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:01:29 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:04:57 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:03:01 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:02:54 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:04:46 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:00:17 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-02 11:25:18 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.008 |  |
| 2026-05-02 11:07:39 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-05-02 11:01:17 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.010 |  |
| 2026-05-02 11:01:47 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-05-02 11:05:34 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-05-02 11:03:14 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-02 11:03:36 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-02 11:01:19 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-05-02 11:26:04 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.016 |  |
| 2026-05-02 11:06:28 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-05-02 11:05:31 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.021 |  |
| 2026-05-02 11:03:17 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | -0.021 |  |
| 2026-05-02 11:02:53 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.023 |  |
| 2026-05-02 11:01:21 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.023 |  |
| 2026-05-02 11:08:58 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.029 |  |
| 2026-05-02 11:03:18 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | -0.029 |  |
| 2026-05-02 11:04:42 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.038 |  |
| 2026-05-02 11:02:17 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.050 |  |
| 2026-05-02 11:02:26 | Glencourse (Kelani Ganga) | 8.86 | 🟢 Normal | -0.071 |  |
| 2026-05-02 11:12:58 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.104 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)