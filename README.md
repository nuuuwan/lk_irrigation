# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--02_22:11:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **168,778 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 22:11:03 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:10:51 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-06-02 22:09:15 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.027 |  |
| 2026-06-02 22:08:09 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:07:59 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:07:38 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:06:52 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.009 |  |
| 2026-06-02 22:06:31 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-02 22:06:19 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:05:18 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-06-02 22:05:04 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:04:46 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-02 22:04:36 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:04:16 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.022 |  |
| 2026-06-02 22:04:14 | Nagalagam Street (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:04:10 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-02 22:04:06 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:03:43 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-02 22:03:26 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:03:13 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.279 | 🔺 Rising |
| 2026-06-02 22:03:12 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:03:01 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:02:51 | Hanwella (Kelani Ganga) | 1.51 | 🟢 Normal | -0.030 |  |
| 2026-06-02 22:02:51 | Glencourse (Kelani Ganga) | 9.69 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-02 22:02:50 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 22:01:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-02 22:01:48 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-02 22:01:29 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-06-02 22:01:24 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-02 22:01:01 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:00:22 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:00:12 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 22:03:13 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.279 | 🔺 Rising |
| 2026-06-02 21:11:41 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-06-02 22:01:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-02 22:04:10 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-02 22:03:43 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-02 22:02:51 | Glencourse (Kelani Ganga) | 9.69 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-02 20:03:23 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-02 22:04:46 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-02 22:06:31 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-02 22:01:48 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-02 22:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-02 22:02:50 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 22:07:38 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-02 18:00:11 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:00:22 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:03:01 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:01:24 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:03:12 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:01:01 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-02 18:00:09 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:06:19 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:04:36 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:08:09 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:04:14 | Nagalagam Street (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:07:59 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:00:12 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:11:03 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-02 21:03:37 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:03:26 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:05:04 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-06-02 18:04:24 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:04:06 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:06:52 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.009 |  |
| 2026-06-02 22:01:29 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-06-02 22:05:18 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-06-02 22:10:51 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-06-02 22:04:16 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.022 |  |
| 2026-06-02 22:09:15 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.027 |  |
| 2026-06-02 22:02:51 | Hanwella (Kelani Ganga) | 1.51 | 🟢 Normal | -0.030 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)