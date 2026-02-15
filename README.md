# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--15_10:14:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **73,618 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 10:14:38 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:14:18 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | -0.018 |  |
| 2026-02-15 10:10:56 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:10:07 | Padiyathalawa (Maduru Oya) | 1.33 | 🟢 Normal | -0.019 |  |
| 2026-02-15 10:08:05 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.074 |  |
| 2026-02-15 10:07:48 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:07:14 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 10:06:33 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-02-15 10:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | -0.088 |  |
| 2026-02-15 10:06:13 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:06:02 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:05:56 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:05:55 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-02-15 10:05:07 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:04:10 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 10:03:55 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.071 |  |
| 2026-02-15 10:03:37 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:03:28 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.068 |  |
| 2026-02-15 10:03:00 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:02:41 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-15 10:02:39 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-15 10:02:38 | Kithulgala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.041 |  |
| 2026-02-15 10:02:33 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-15 10:02:24 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.021 |  |
| 2026-02-15 10:02:21 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-02-15 10:02:07 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:02:04 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.015 |  |
| 2026-02-15 10:01:48 | Manampitiya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.255 | 🔺 Rising |
| 2026-02-15 10:01:47 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-02-15 10:01:45 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-02-15 10:01:43 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.037 |  |
| 2026-02-15 10:01:37 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:01:18 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:01:13 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:01:10 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:01:02 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:00:50 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:00:41 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.040 |  |
| 2026-02-15 10:00:11 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | 0.165 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 10:01:48 | Manampitiya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.255 | 🔺 Rising |
| 2026-02-15 10:00:11 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-02-15 10:01:45 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-02-15 10:02:41 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-15 10:02:33 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-15 10:02:39 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-15 10:07:14 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 10:04:10 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 10:01:37 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:14:38 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:06:02 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:01:02 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:03:00 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:10:56 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:01:10 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:05:56 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:02:07 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:05:07 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:03:37 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:07:48 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:00:50 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:06:13 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:01:13 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:01:18 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-15 10:05:55 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-02-15 10:01:47 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-02-15 10:02:04 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.015 |  |
| 2026-02-15 10:14:18 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | -0.018 |  |
| 2026-02-15 10:10:07 | Padiyathalawa (Maduru Oya) | 1.33 | 🟢 Normal | -0.019 |  |
| 2026-02-15 10:02:21 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-02-15 10:02:24 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.021 |  |
| 2026-02-15 10:06:33 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-02-15 10:01:43 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.037 |  |
| 2026-02-15 10:00:41 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.040 |  |
| 2026-02-15 10:02:38 | Kithulgala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.041 |  |
| 2026-02-15 10:03:28 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.068 |  |
| 2026-02-15 10:03:55 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.071 |  |
| 2026-02-15 10:08:05 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.074 |  |
| 2026-02-15 10:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)