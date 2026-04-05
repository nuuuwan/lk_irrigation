# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_06:13:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **116,580 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 06:13:51 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-05 06:13:10 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | -0.028 |  |
| 2026-04-05 06:10:20 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | -36.000 |  |
| 2026-04-05 06:10:19 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -36.000 |  |
| 2026-04-05 06:09:00 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | -0.009 |  |
| 2026-04-05 06:08:03 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.049 |  |
| 2026-04-05 06:07:26 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-05 06:05:48 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.023 |  |
| 2026-04-05 06:05:45 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-05 06:05:21 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-05 06:04:51 | Siyambalanduwa (Heda Oya) | 0.91 | 🟢 Normal | -0.057 |  |
| 2026-04-05 06:04:23 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.090 |  |
| 2026-04-05 06:03:32 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.041 |  |
| 2026-04-05 06:03:26 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.041 |  |
| 2026-04-05 06:03:20 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-05 06:03:04 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-05 06:03:01 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.059 |  |
| 2026-04-05 06:02:59 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-04-05 06:02:46 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-05 06:02:44 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-05 06:02:43 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-05 06:02:28 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-05 06:02:27 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.012 |  |
| 2026-04-05 06:02:25 | Manampitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.031 |  |
| 2026-04-05 06:02:23 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-05 06:02:22 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-04-05 06:02:13 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 06:02:00 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-05 06:01:53 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-04-05 06:01:51 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.151 |  |
| 2026-04-05 06:01:36 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-05 06:01:31 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 06:01:20 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 06:01:20 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-04-05 06:01:15 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-04-05 06:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.37 | 🟢 Normal | 0.728 | 🔺 Rising |
| 2026-04-05 06:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-04-05 06:00:45 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-05 06:00:37 | Weraganthota (Mahaweli Ganga) | -2.16 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-05 06:00:10 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-05 05:50:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | 0.728 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 06:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.37 | 🟢 Normal | 0.728 | 🔺 Rising |
| 2026-04-05 06:01:15 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-04-05 06:02:59 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-04-05 06:00:37 | Weraganthota (Mahaweli Ganga) | -2.16 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-05 06:02:00 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-05 06:05:21 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-05 06:01:36 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-05 06:02:28 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-05 06:03:20 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-05 06:03:04 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-05 06:02:13 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 06:13:51 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-05 06:00:10 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-05 06:01:31 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 06:01:20 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:58:33 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-05 06:01:53 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-04-05 06:02:46 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-05 06:00:45 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-05 06:07:26 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-05 06:01:20 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-04-05 06:09:00 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | -0.009 |  |
| 2026-04-05 06:05:45 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-05 06:02:23 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-05 06:02:27 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.012 |  |
| 2026-04-05 06:02:22 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-04-05 06:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-04-05 06:05:48 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.023 |  |
| 2026-04-05 06:13:10 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | -0.028 |  |
| 2026-04-04 18:01:01 | Thanthirimale (Malwathu Oya) | 2.52 | 🟢 Normal | -0.031 |  |
| 2026-04-05 06:02:25 | Manampitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.031 |  |
| 2026-04-05 06:03:26 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.041 |  |
| 2026-04-05 06:03:32 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.041 |  |
| 2026-04-05 06:08:03 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.049 |  |
| 2026-04-05 06:04:51 | Siyambalanduwa (Heda Oya) | 0.91 | 🟢 Normal | -0.057 |  |
| 2026-04-05 06:03:01 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.059 |  |
| 2026-04-05 06:04:23 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.090 |  |
| 2026-04-05 06:01:51 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.151 |  |
| 2026-04-05 06:10:20 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)