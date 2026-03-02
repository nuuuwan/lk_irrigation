# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--02_08:04:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **86,975 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 08:04:59 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-02 08:04:58 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:04:54 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.127 |  |
| 2026-03-02 08:04:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | -0.062 |  |
| 2026-03-02 08:04:33 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:04:27 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:04:21 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:04:11 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-02 08:03:56 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.046 |  |
| 2026-03-02 08:03:55 | Hanwella (Kelani Ganga) | 0.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-02 08:03:26 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-02 08:03:22 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:03:09 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-02 08:02:38 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:02:28 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | -0.030 |  |
| 2026-03-02 08:02:07 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-03-02 08:01:41 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-03-02 08:01:14 | Weraganthota (Mahaweli Ganga) | -1.78 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-02 08:01:12 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.053 |  |
| 2026-03-02 08:01:11 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:01:05 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-03-02 08:01:00 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:00:41 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | -0.019 |  |
| 2026-03-02 07:58:48 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.104 |  |
| 2026-03-02 07:48:57 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.048 |  |
| 2026-03-02 07:28:32 | Horowpothana (Yan Oya) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-03-02 07:28:16 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 07:19:01 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-02 07:14:33 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-02 07:12:21 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-02 07:11:21 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-02 07:11:12 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.046 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 08:01:14 | Weraganthota (Mahaweli Ganga) | -1.78 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-02 08:04:59 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-02 07:03:37 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-02 08:03:55 | Hanwella (Kelani Ganga) | 0.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-02 08:03:09 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-02 08:03:26 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-02 08:04:11 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-02 08:01:00 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:04:21 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 07:01:40 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:04:27 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-02 07:10:21 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-02 07:03:25 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:03:22 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-02 07:08:23 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-02 07:03:33 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-03-02 07:14:33 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-02 07:05:45 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:02:38 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:01:11 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:04:58 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 07:19:01 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-02 07:28:16 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 07:03:30 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-03-02 08:01:05 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-03-02 07:03:14 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-03-02 07:10:37 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.017 |  |
| 2026-03-02 08:00:41 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | -0.019 |  |
| 2026-03-02 08:01:41 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-03-02 08:02:07 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-03-02 08:02:28 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | -0.030 |  |
| 2026-03-02 07:04:21 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.033 |  |
| 2026-03-02 08:03:56 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.046 |  |
| 2026-03-02 07:48:57 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.048 |  |
| 2026-03-02 08:01:12 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.053 |  |
| 2026-03-02 08:04:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | -0.062 |  |
| 2026-03-02 07:58:48 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.104 |  |
| 2026-03-02 08:04:54 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)