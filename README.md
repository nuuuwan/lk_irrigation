# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--16_10:18:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **74,507 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-16 10:18:35 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:13:25 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.078 |  |
| 2026-02-16 10:11:21 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:11:08 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:10:30 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-02-16 10:10:15 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 8.636 | 🔺 Rising |
| 2026-02-16 10:09:51 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.005 |  |
| 2026-02-16 10:07:06 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-02-16 10:06:51 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-02-16 10:06:48 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-16 10:06:01 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:05:45 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:05:15 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:04:21 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:04:11 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.031 |  |
| 2026-02-16 10:04:04 | Thawalama (Gin Ganga) | 0.23 | 🟢 Normal | 8.636 | 🔺 Rising |
| 2026-02-16 10:03:44 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-02-16 10:03:15 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-02-16 10:03:04 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:03:01 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-16 10:02:58 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.233 |  |
| 2026-02-16 10:02:54 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.020 |  |
| 2026-02-16 10:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.040 |  |
| 2026-02-16 10:02:19 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -1.103 |  |
| 2026-02-16 10:02:16 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:02:12 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-16 10:02:05 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:01:47 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | -0.043 |  |
| 2026-02-16 10:01:45 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-02-16 10:01:29 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-02-16 10:01:25 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:01:23 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:01:13 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:01:09 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:01:08 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-02-16 10:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:01:01 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:00:46 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:00:39 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-16 09:57:41 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | 0.000 |  |
| 2026-02-16 09:57:15 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-16 10:10:15 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 8.636 | 🔺 Rising |
| 2026-02-16 10:06:48 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-16 10:06:51 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-02-16 10:03:01 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-16 10:02:12 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-16 10:01:09 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:11:08 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:02:05 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:02:16 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:11:21 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:01:23 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:01:01 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:03:04 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:01:13 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:00:39 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:01:25 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:06:01 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:05:45 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:18:35 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:05:15 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:04:21 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:00:46 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:09:51 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.005 |  |
| 2026-02-16 10:10:30 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-02-16 09:06:41 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.009 |  |
| 2026-02-16 10:03:44 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-02-16 10:01:45 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-02-16 10:03:15 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-02-16 10:01:08 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-02-16 10:07:06 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-02-16 10:02:54 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.020 |  |
| 2026-02-16 10:01:29 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-02-16 10:04:11 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.031 |  |
| 2026-02-16 10:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.040 |  |
| 2026-02-16 10:01:47 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | -0.043 |  |
| 2026-02-16 10:13:25 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.078 |  |
| 2026-02-16 10:02:58 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.233 |  |
| 2026-02-16 10:02:19 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -1.103 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)