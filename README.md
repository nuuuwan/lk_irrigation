# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--02_07:01:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **168,171 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 07:01:58 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.011 |  |
| 2026-06-02 07:01:57 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 07:01:36 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-02 07:01:36 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-06-02 07:01:34 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | -0.033 |  |
| 2026-06-02 07:01:29 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.030 |  |
| 2026-06-02 07:01:21 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-02 07:01:21 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | -0.021 |  |
| 2026-06-02 07:01:10 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-06-02 07:01:09 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 07:00:46 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | -0.003 |  |
| 2026-06-02 07:00:07 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-02 06:59:53 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-02 06:31:13 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.002 |  |
| 2026-06-02 06:30:16 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-02 06:15:39 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-02 06:15:10 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-06-02 06:14:56 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-06-02 06:14:43 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-06-02 06:14:29 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-06-02 06:14:15 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-06-02 06:14:02 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-06-02 06:13:49 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 07:01:36 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-06-02 06:04:42 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-06-02 06:15:39 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-02 06:02:17 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-02 06:06:13 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-02 07:01:09 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 06:03:46 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 06:05:50 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 06:05:57 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 06:00:27 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-02 07:01:57 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 06:30:16 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-02 06:03:39 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 06:00:28 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-02 06:02:00 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-02 06:04:06 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-02 06:15:10 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-06-02 07:01:21 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-02 06:05:31 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-02 06:02:54 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-02 06:00:23 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-02 07:01:36 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-02 06:31:13 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.002 |  |
| 2026-06-02 07:00:46 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | -0.003 |  |
| 2026-06-02 06:07:47 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-06-02 07:01:10 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-06-02 07:00:07 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-02 07:01:58 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.011 |  |
| 2026-06-02 06:03:55 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-06-02 06:02:16 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | -0.011 |  |
| 2026-06-02 06:03:43 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.020 |  |
| 2026-06-02 06:01:55 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-06-02 07:01:21 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | -0.021 |  |
| 2026-06-02 07:01:29 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.030 |  |
| 2026-06-02 07:01:34 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | -0.033 |  |
| 2026-06-02 06:02:10 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.053 |  |
| 2026-06-02 06:01:24 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.054 |  |
| 2026-06-02 06:04:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | -0.056 |  |
| 2026-06-02 06:05:28 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)