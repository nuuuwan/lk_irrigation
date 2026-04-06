# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_10:18:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,628 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 10:18:30 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.043 |  |
| 2026-04-06 10:13:15 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.058 |  |
| 2026-04-06 10:09:48 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:08:26 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.133 |  |
| 2026-04-06 10:07:19 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:06:15 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:05:37 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-04-06 10:05:26 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:05:17 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.011 |  |
| 2026-04-06 10:05:14 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:04:58 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.019 |  |
| 2026-04-06 10:04:54 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.062 |  |
| 2026-04-06 10:04:08 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:04:01 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:03:52 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-06 10:03:51 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.101 |  |
| 2026-04-06 10:03:45 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-04-06 10:03:14 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:03:13 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.067 |  |
| 2026-04-06 10:03:08 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 10:03:04 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 10:03:01 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:02:58 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.110 |  |
| 2026-04-06 10:02:45 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:02:39 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:02:26 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | -0.011 |  |
| 2026-04-06 10:02:21 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.030 |  |
| 2026-04-06 10:02:16 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-04-06 10:02:15 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-04-06 10:02:12 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-06 10:02:07 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:01:24 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:01:17 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-04-06 10:01:17 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:00:58 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:00:45 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | -0.020 |  |
| 2026-04-06 10:00:14 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | -0.052 |  |
| 2026-04-06 10:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:00:11 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 10:03:52 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-06 10:03:04 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 10:03:08 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 10:04:08 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:00:11 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:02:07 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:03:45 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:07:19 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:03:14 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:01:24 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:01:17 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:05:26 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:02:39 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:00:58 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:06:15 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:03:01 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:05:14 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:09:48 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:04:01 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-06 10:02:16 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-04-06 10:02:12 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-06 10:02:15 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-04-06 10:02:26 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | -0.011 |  |
| 2026-04-06 10:05:17 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.011 |  |
| 2026-04-06 10:04:58 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.019 |  |
| 2026-04-06 10:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-04-06 10:00:45 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | -0.020 |  |
| 2026-04-06 10:05:37 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-04-06 10:01:17 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-04-06 10:02:21 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.030 |  |
| 2026-04-06 10:18:30 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.043 |  |
| 2026-04-06 10:00:14 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | -0.052 |  |
| 2026-04-06 10:13:15 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.058 |  |
| 2026-04-06 10:04:54 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.062 |  |
| 2026-04-06 10:03:13 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.067 |  |
| 2026-04-06 10:03:51 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.101 |  |
| 2026-04-06 10:02:58 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.110 |  |
| 2026-04-06 10:08:26 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)