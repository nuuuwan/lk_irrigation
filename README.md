# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_08:27:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,707 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 08:27:34 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-05-02 08:11:36 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.021 |  |
| 2026-05-02 08:10:31 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-05-02 08:10:12 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.034 |  |
| 2026-05-02 08:07:52 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-02 08:07:33 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-05-02 08:05:28 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 08:04:43 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-02 08:04:43 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.039 |  |
| 2026-05-02 08:04:40 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-05-02 08:04:31 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-02 08:04:27 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.019 |  |
| 2026-05-02 08:04:21 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.093 |  |
| 2026-05-02 08:04:14 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-02 08:04:05 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.032 |  |
| 2026-05-02 08:03:45 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-05-02 08:03:42 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-02 08:03:31 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.029 |  |
| 2026-05-02 08:03:18 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-05-02 08:03:04 | Glencourse (Kelani Ganga) | 9.07 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-02 08:02:58 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-02 08:02:54 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.022 |  |
| 2026-05-02 08:02:36 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 08:02:32 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-02 08:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.040 |  |
| 2026-05-02 08:02:17 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-05-02 08:02:12 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-02 08:01:48 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.000 |  |
| 2026-05-02 08:01:46 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-02 08:01:38 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-02 08:01:37 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-02 08:01:09 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.053 |  |
| 2026-05-02 08:00:58 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-02 08:00:57 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 08:00:55 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-02 08:00:50 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-05-02 08:00:36 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.021 |  |
| 2026-05-02 08:00:24 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-02 08:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-05-02 07:48:01 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 08:10:31 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-05-02 08:04:14 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-02 08:00:24 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-02 08:04:43 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-02 08:01:37 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-02 08:03:04 | Glencourse (Kelani Ganga) | 9.07 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-02 08:01:38 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-02 08:05:28 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 08:02:36 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 08:27:34 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-05-02 08:02:58 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-02 08:07:52 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-02 08:00:57 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 08:02:12 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-02 08:00:55 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-02 08:01:48 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.000 |  |
| 2026-05-02 07:48:01 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-02 08:02:32 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-02 08:00:58 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-02 08:03:42 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-02 08:04:31 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-02 08:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-05-02 08:02:17 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-05-02 08:00:50 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-05-02 08:03:45 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-05-02 08:07:33 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-05-02 08:03:18 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-05-02 08:04:27 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.019 |  |
| 2026-05-02 08:04:40 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-05-02 08:00:36 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.021 |  |
| 2026-05-02 08:11:36 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.021 |  |
| 2026-05-02 08:02:54 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.022 |  |
| 2026-05-02 08:03:31 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.029 |  |
| 2026-05-02 08:04:05 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.032 |  |
| 2026-05-02 08:10:12 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.034 |  |
| 2026-05-02 08:04:43 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.039 |  |
| 2026-05-02 08:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.040 |  |
| 2026-05-02 08:01:09 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.053 |  |
| 2026-05-02 08:04:21 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)