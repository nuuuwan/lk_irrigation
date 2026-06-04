# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--04_07:33:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **170,010 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 07:33:59 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-04 07:31:09 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-04 07:31:07 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-04 07:29:08 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-06-04 07:27:11 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-04 07:15:02 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 07:11:11 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-04 07:10:05 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-06-04 07:09:24 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-06-04 07:08:53 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-04 07:08:52 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-04 07:08:49 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-04 07:08:49 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-04 07:08:06 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-04 07:07:48 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-04 07:07:44 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-04 07:07:05 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 07:05:30 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-06-04 07:05:26 | Rathnapura (Kalu Ganga) | 2.56 | 🟢 Normal | -0.011 |  |
| 2026-06-04 07:05:01 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-04 07:05:00 | Hanwella (Kelani Ganga) | 2.14 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-04 07:04:58 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.056 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 07:09:24 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-06-04 07:02:20 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-06-04 07:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-06-04 07:02:45 | Ellagawa (Kalu Ganga) | 5.89 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-06-04 07:05:00 | Hanwella (Kelani Ganga) | 2.14 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-04 07:08:49 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-04 07:02:28 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-06-04 07:08:49 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-04 07:33:59 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-04 07:27:11 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-04 07:02:51 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-04 07:02:29 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-04 07:08:52 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-04 07:07:44 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-04 07:07:05 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 07:08:06 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-04 07:05:30 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-06-04 07:00:24 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-04 07:01:05 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 07:15:02 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 07:01:41 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 07:05:01 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-04 07:31:09 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-04 07:02:18 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 07:07:48 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-04 07:08:53 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-04 07:29:08 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-06-04 07:00:47 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | -0.002 |  |
| 2026-06-04 07:11:11 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-04 07:03:01 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.011 |  |
| 2026-06-04 07:05:26 | Rathnapura (Kalu Ganga) | 2.56 | 🟢 Normal | -0.011 |  |
| 2026-06-04 07:00:27 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-06-04 07:01:29 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.012 |  |
| 2026-06-04 07:10:05 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-06-04 07:00:29 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | -0.025 |  |
| 2026-06-04 07:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.030 |  |
| 2026-06-04 07:04:58 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.056 |  |
| 2026-06-04 07:02:58 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | -0.057 |  |
| 2026-06-04 07:02:56 | Deraniyagala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)