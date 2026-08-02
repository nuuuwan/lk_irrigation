# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_09:14:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **222,766 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 09:14:09 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-08-02 09:11:24 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:09:55 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-02 09:09:17 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:08:57 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:08:04 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-08-02 09:07:58 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.066 |  |
| 2026-08-02 09:06:41 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | -0.041 |  |
| 2026-08-02 09:05:38 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:05:26 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | -0.030 |  |
| 2026-08-02 09:05:22 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.011 |  |
| 2026-08-02 09:05:16 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:04:54 | Hanwella (Kelani Ganga) | 2.44 | 🟢 Normal | -0.149 |  |
| 2026-08-02 09:04:27 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:04:27 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | -0.095 |  |
| 2026-08-02 09:04:19 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:04:14 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-08-02 09:04:11 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.019 |  |
| 2026-08-02 09:04:06 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:03:50 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-02 09:03:41 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | -0.029 |  |
| 2026-08-02 09:03:31 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:03:31 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | -0.078 |  |
| 2026-08-02 09:03:08 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:03:02 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:03:01 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.49 | 🟢 Normal | -0.026 |  |
| 2026-08-02 09:02:46 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-08-02 09:02:10 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:02:00 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:01:52 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-02 09:01:47 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.012 |  |
| 2026-08-02 09:01:44 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-08-02 09:01:43 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-08-02 09:01:33 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:01:33 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:01:31 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-08-02 09:00:48 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 09:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-08-02 09:01:44 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-08-02 09:01:52 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-02 09:14:09 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-08-02 09:09:55 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-02 09:03:50 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-02 09:00:48 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 09:02:00 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:11:24 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:04:27 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:09:17 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:04:19 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:05:38 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:01:31 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-08-02 08:11:29 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:03:02 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:04:06 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:03:08 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:02:10 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:03:01 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:01:33 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:03:31 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:08:57 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:01:33 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:04:14 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-08-02 09:02:46 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-08-02 09:08:04 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-08-02 09:05:22 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.011 |  |
| 2026-08-02 09:01:47 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.012 |  |
| 2026-08-02 09:04:11 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.019 |  |
| 2026-08-02 09:01:43 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-08-02 09:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.49 | 🟢 Normal | -0.026 |  |
| 2026-08-02 09:03:41 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | -0.029 |  |
| 2026-08-02 09:05:26 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | -0.030 |  |
| 2026-08-02 09:06:41 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | -0.041 |  |
| 2026-08-02 09:07:58 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.066 |  |
| 2026-08-02 09:03:31 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | -0.078 |  |
| 2026-08-02 09:04:27 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | -0.095 |  |
| 2026-08-02 09:04:54 | Hanwella (Kelani Ganga) | 2.44 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)