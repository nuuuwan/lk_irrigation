# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--02_01:28:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **194,811 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-02 01:28:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | -0.018 |  |
| 2026-07-02 01:22:02 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.091 |  |
| 2026-07-02 01:21:22 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:13:53 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:11:29 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:10:05 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.009 |  |
| 2026-07-02 01:08:56 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-02 01:06:33 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -18.000 |  |
| 2026-07-02 01:06:31 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -18.000 |  |
| 2026-07-02 01:05:53 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:05:48 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-07-02 01:05:42 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-07-02 01:05:14 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:05:00 | Rathnapura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-07-02 01:04:49 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:04:49 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-07-02 01:04:39 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.021 |  |
| 2026-07-02 01:04:33 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:04:33 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-02 01:03:49 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:03:00 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:02:57 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.053 |  |
| 2026-07-02 01:02:42 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-07-02 01:02:19 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-02 00:03:42 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-07-02 01:04:49 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-07-02 01:08:56 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-02 01:04:33 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-02 00:15:40 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-07-01 18:02:29 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:11:29 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:01:29 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:15:01 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:01:31 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:01:20 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:06:53 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:01:09 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:05:53 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:21:22 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:13:53 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:06:10 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:03:49 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:03:20 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:05:14 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:04:07 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:02:02 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:04:49 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:03:00 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:10:05 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.009 |  |
| 2026-07-02 01:05:00 | Rathnapura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-07-02 01:02:42 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-07-02 01:05:48 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-07-02 01:02:19 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-07-02 01:28:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | -0.018 |  |
| 2026-07-02 01:05:42 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-07-02 01:01:24 | Hanwella (Kelani Ganga) | 1.67 | 🟢 Normal | -0.020 |  |
| 2026-07-02 01:04:39 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.021 |  |
| 2026-07-02 00:43:49 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.028 |  |
| 2026-07-02 01:02:57 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.053 |  |
| 2026-07-02 01:01:45 | Peradeniya (Mahaweli Ganga) | 2.29 | 🟢 Normal | -0.074 |  |
| 2026-07-02 01:22:02 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.091 |  |
| 2026-07-02 01:06:33 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -18.000 |  |
| 2026-07-02 00:02:58 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)